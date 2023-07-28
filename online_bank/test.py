def calculate_solar_system():
    # Step 1: Gather Location-specific Solar Data (Example Values)
    sunshine_hours = 5.5  # Average daily sunshine hours
    average_temperature = 25.0  # Average temperature in Celsius

    # Step 2: Get User Inputs
    total_load_rating = float(input("Enter total load rating in kilowatts: "))
    daily_usage = float(input("Enter expected daily usage in hours: "))

    # Step 3: Estimate Daily Energy Consumption
    daily_energy_consumption = total_load_rating * daily_usage

    # Step 4: Solar Panel Sizing
    solar_panel_efficiency = 0.15  # Example solar panel efficiency (15%)
    solar_panel_capacity = daily_energy_consumption / (sunshine_hours * solar_panel_efficiency)

    # Step 5: Inverter Sizing
    inverter_efficiency = 0.9  # Example inverter efficiency (90%)
    inverter_capacity = daily_energy_consumption / (sunshine_hours * inverter_efficiency)

    # Step 6: Charge Controller Sizing
    charge_controller_efficiency = 0.95  # Example charge controller efficiency (95%)
    charge_controller_capacity = inverter_capacity / charge_controller_efficiency

    # Step 7: Cable Sizing
    cable_size = inverter_capacity * 1.25  # Example cable sizing with 25% safety margin

    # Step 8: Battery Sizing
    battery_backup_days = 1  # Example of 1-day backup
    battery_capacity = daily_energy_consumption * battery_backup_days

    # Step 9: Display Results
    print("\nSolar Energy System Estimation:")
    print(f"Solar Panel Rating (kW): {solar_panel_capacity:.2f}")
    print(f"Inverter Rating (kW): {inverter_capacity:.2f}")
    print(f"Charge Controller Rating (A): {charge_controller_capacity:.2f}")
    print(f"Cable Size (mm^2): {cable_size:.2f}")
    print(f"Battery Capacity (kWh): {battery_capacity:.2f}")


if __name__ == "__main__":
    calculate_solar_system()
