Хорошо 💫 Я сделаю для твоего проекта понятный и структурированный README.md.
Он будет включать описание, установку, использование и пример работы.

# React Element Generator

Скрипт для автоматизированного создания файлов React-компонентов.  
Позволяет в интерактивном режиме создавать структуру с **`.tsx`**, **`.module.css`** и **`index.ts`** файлами в папке `src/components` или `src/pages`.

## 🚀 Возможности

- Создание пустых файлов компонентов с готовой базовой разметкой:
  - `<Name>.tsx`
  - `<Name>.module.css`
  - `index.ts`
- Автоматическая генерация структуры папок внутри `src/components` или `src/pages`.
- Интерактивный CLI-режим с подтверждением перед созданием файлов.
- Красивый вывод в консоли с подсветкой.

## 📂 Пример структуры

Если выбрать `components` и ввести `MyCourses/AuthorCourses`, то скрипт создаст:

src/
└── components/
└── MyCourses/
└── AuthorCourses/
├── AuthorCourses.tsx
├── AuthorCourses.module.css
└── index.ts

## ⚙️ Установка

1. Клонируй репозиторий или скопируй скрипт в свой проект.
2. Убедись, что у тебя установлен **Python 3.10+**.
3. Запусти:

```bash
python main.py

🖥️ Использование

После запуска программа задаст несколько вопросов:
	1.	Выбор базовой папки:

c - components, p - pages:

Введи c или p.

	2.	Название элемента:

Куда кладем? components/

Введи название компонента или путь, например:
	•	AuthorCourses
	•	MyCourses/AuthorCourses

	3.	Подтверждение перед созданием:

Итак, создаём файлы:
    components/MyCourses/AuthorCourses/AuthorCourses.tsx
    components/MyCourses/AuthorCourses/AuthorCourses.module.css
    components/MyCourses/AuthorCourses/index.ts

Ок? [Y]/N:



Если нажать Enter или Y, файлы будут созданы.

📄 Пример сгенерированного файла

AuthorCourses.tsx:

import styles from "./AuthorCourses.module.css"

interface AuthorCoursesProps {
    
}

const AuthorCourses = ({}: AuthorCoursesProps) => (
  <div>AuthorCourses</div>
)

export default AuthorCourses

AuthorCourses.module.css – пока пустой.
index.ts:

export { default } from "./AuthorCourses";

💡 Идеи для улучшения
	•	Добавить шаблоны для разных типов компонентов (например, с хуками или с props).
	•	Возможность отключать генерацию index.ts.
	•	Поддержка тестов (.test.tsx).
	•	Конфигурация через config.json.
