import sys
import subprocess
from typing import Optional

def get_cpu_temperature() -> Optional[str]:
    """
    Возвращает текущую температуру CPU в градусах Цельсия.
    На macOS используется powermetrics или osx-cpu-temp, на Linux – psutil.
    """
    # Если система – macOS, используем powermetrics или osx-cpu-temp
    if sys.platform == "darwin":
        # Попробуем вызвать osx-cpu-temp (нужно установить, например через Homebrew)
        try:
            output = subprocess.check_output(["osx-cpu-temp"], text=True)
            temp = output.strip()
            return f"Температура CPU: {temp}"
        except FileNotFoundError:
            # Если утилита osx-cpu-temp не установлена, пробуем powermetrics
            try:
                # Запуск powermetrics для одного замера (опция -n1)
                result = subprocess.run(
                    ["sudo", "powermetrics", "--samplers", "smc", "-n1"],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
                )
                if result.returncode == 0:
                    # Ищем строку с "CPU die temperature"
                    for line in result.stdout.splitlines():
                        if "CPU die temperature:" in line:
                            temp_str = line.split("CPU die temperature:")[-1].strip()
                            return f"Температура CPU: {temp_str}"
                    return "Температура CPU не найдена в выводе powermetrics."
                else:
                    # powermetrics вернул ошибку (например, без sudo)
                    return f"Ошибка powermetrics: {result.stderr.strip()}"
            except Exception as e:
                return f"Не удалось вызвать powermetrics: {e}"
    # На других системах – Linux/Windows – используем psutil (поддержка Linux)
    try:
        temps = psutil.sensors_temperatures()
    except AttributeError:
        return "psutil не поддерживает датчики температуры на этой платформе."
    if not temps:
        return "Температурные датчики не найдены."
    # Для AMD (k10temp) или другие ядра
    if "k10temp" in temps:
        for entry in temps["k10temp"]:
            if entry.label in ("Tctl", "Tdie"):
                return f"Температура CPU: {entry.current:.1f}°C"
        return "Сенсор 'k10temp' найден, но метка Tctl отсутствует."
    for entries in temps.values():
        for entry in entries:
            label = entry.label.lower()
            if label.startswith("package") or "core" in label:
                return f"Температура CPU: {entry.current:.1f}°C"
    return "Не удалось определить температуру CPU."

if __name__ == "__main__":
    print(get_cpu_temperature())