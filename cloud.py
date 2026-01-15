# Cloud Computing Assignment
# Simple Cloud Service Cost Calculator

print("Calculating Cloud Service Cost")

# Input from user
storage = float(input("Enter storage used (in GB): "))
hours_used = float(input("Enter compute hours used: "))

# Cost rates (example values)
storage_cost_per_gb = 10    # ₹5 per GB
compute_cost_per_hour = 15  # ₹10 per hour

# Calculate total cost
total_storage_cost = storage * storage_cost_per_gb
total_compute_cost = hours_used * compute_cost_per_hour
total_cost = total_storage_cost + total_compute_cost

# Display output
print("\n--- Cost Details ---")
print("Storage Cost: ₹", total_storage_cost)
print("Compute Cost: ₹", total_compute_cost)
print("Total Cloud Usage Cost: ₹", total_cost)
