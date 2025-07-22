import CoreLocation

let manager = CLLocationManager()
manager.requestAlwaysAuthorization()

if CLLocationManager.locationServicesEnabled() {
    if let location = manager.location {
        print("Широта: \(location.coordinate.latitude)")
        print("Долгота: \(location.coordinate.longitude)")
    } else {
        print("Геоданные не получены.")
    }
} else {
    print("Геолокация отключена.")
}