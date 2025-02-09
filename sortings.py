
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def get_user_input():
    try:
        n = int(input("Enter the number of elements: "))
        arr = []
        print(f"Enter {n} numbers:")
        for i in range(n):
            num = float(input(f"Enter number {i+1}: "))
            arr.append(num)
        return arr
    except ValueError:
        print("Please enter valid numbers!")
        return None

def display_menu():
    print("\nChoose a sorting algorithm:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Exit")
    return input("Enter your choice (1-4): ")

def main():
    while True:
        choice = display_menu()
        
        if choice == '4':
            print("Goodbye!")
            break
            
        if choice not in ['1', '2', '3']:
            print("Invalid choice! Please select 1-4")
            continue
            
        # Get input from user
        arr = get_user_input()
        
        if arr is not None:
            print("\nOriginal array:", arr)
            
            # Apply selected sorting algorithm
            if choice == '1':
                sorted_arr = bubble_sort(arr.copy())
                print("Sorted array (Bubble Sort):", sorted_arr)
            elif choice == '2':
                sorted_arr = selection_sort(arr.copy())
                print("Sorted array (Selection Sort):", sorted_arr)
            elif choice == '3':
                sorted_arr = insertion_sort(arr.copy())
                print("Sorted array (Insertion Sort):", sorted_arr)

if __name__ == "__main__":
    main()