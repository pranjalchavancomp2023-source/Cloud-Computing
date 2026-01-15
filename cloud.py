# Cloud Computing Assignment
# Simple Cloud Service Cost Calculator

print("Cloud Service Cost Calculator")

# Input from user
storage_gb = float(input("Enter storage used (in GB): "))
compute_hours = float(input("Enter compute hours used: "))

# Cost rates (example values)
storage_cost_per_gb = 5     # ₹5 per GB
compute_cost_per_hour = 10  # ₹10 per hour

# Calculate total cost
total_storage_cost = storage_gb * storage_cost_per_gb
total_compute_cost = compute_hours * compute_cost_per_hour
total_cost = total_storage_cost + total_compute_cost

# Display output
print("\n--- Cost Details ---")
print("Storage Cost: ₹", total_storage_cost)
print("Compute Cost: ₹", total_compute_cost)
print("Total Cloud Usage Cost: ₹", total_cost)
