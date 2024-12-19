items = ["Shortsword", "Healing Potion", "Iron Breastplate", "Kite Shield"]

def reverse_array(items):
    new_array= []
    for each_item in range(len(items)-1, -1, -1):
        new_array.append(items[each_item])
    print(new_array)






reverse_array(items)