def count_unserviced_customers(N, S):
    in_cafe = set()         
    using_computer = set() 
    available_computers = N
    walked_away = 0

    for customer in S:
        if customer not in in_cafe:
            in_cafe.add(customer)
            if available_computers > 0:
                using_computer.add(customer)
                available_computers -= 1
            else:
                walked_away += 1
        else:
            in_cafe.remove(customer)
            if customer in using_computer:
                using_computer.remove(customer)
                available_computers += 1

    return walked_away

# Example usage
print(count_unserviced_customers(3, "GACCBDDBAGEE"))  
print(count_unserviced_customers(1, "ABCBAC"))       
