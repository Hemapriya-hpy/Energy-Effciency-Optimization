def calculate_hvac_energy(room_area_sqm, hours_per_day, days_per_month,
                          cooling_capacity_kw, efficiency_ratio, rate_per_kwh):
    """
    Estimate the monthly energy usage and cost of an HVAC system.

    :param room_area_sqm: Room area in square meters (sqm)
    :param hours_per_day: Average daily HVAC usage in hours
    :param days_per_month: Number of days used in a month
    :param cooling_capacity_kw: HVAC system capacity in kilowatts (kW)
    :param efficiency_ratio: Energy Efficiency Ratio (EER) or Coefficient of Performance (COP)
    :param rate_per_kwh: Cost rate per kilowatt-hour (kWh)
    :return: energy_used_kwh, total_cost
    """

    # Energy used per hour (in kWh) = cooling capacity / efficiency ratio
    energy_per_hour_kwh = cooling_capacity_kw / efficiency_ratio

    # Total energy used in the month (kWh)
    total_energy_kwh = energy_per_hour_kwh * hours_per_day * days_per_month

    # Total cost
    total_cost = total_energy_kwh * rate_per_kwh

    return round(total_energy_kwh, 2), round(total_cost, 2)


# Example usage
if __name__ == "__main__":
    print("=== HVAC Energy Usage Calculator ===")

    # User inputs
    room_area = float(input("Enter room area (in square meters): "))
    hours_per_day = float(input("Enter average daily HVAC usage (hours): "))
    days_per_month = int(input("Enter number of days used in a month: "))
    cooling_capacity_kw = float(input("Enter HVAC capacity (kW): "))
    efficiency_ratio = float(input("Enter system efficiency ratio (EER/COP): "))
    rate_per_kwh = float(input("Enter electricity rate (per kWh): "))

    # Calculate
    energy_used, total_cost = calculate_hvac_energy(
        room_area,
        hours_per_day,
        days_per_month,
        cooling_capacity_kw,
        efficiency_ratio,
        rate_per_kwh
    )

    print(f"\nEstimated Energy Used: {energy_used} kWh/month")
    print(f"Estimated Total Cost: {total_cost} currency units/month")

