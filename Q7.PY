# Q7: Lambda function for squares
def square_program():
    # Lambda function square sathi
    square = lambda x: x ** 2
    
    try:
        # 1 to 20 paryant numbers generate kar
        squares_list = []
        for num in range(1, 21):
            squares_list.append(square(num))
        
        print(f"All Squares 1-20: {squares_list}")
        
        # Fakt even squares print kar
        even_squares = [sq for sq in squares_list if sq % 2 == 0]
        print(f"Even Squares Only: {even_squares}")
        
    except Exception as e:
        print(f"Error occurred: {e}")

square_program()