# Create a function to calculate accuracy and precision metrics
def calculate_metrics(tp, fp, fn, tn):
    accuracy = round((tp + tn) / (tp + fp + fn + tn), 2)  # Arredonda para 2 casas decimais
    precision = round(tp / (tp + fp), 2)  # Arredonda para 2 casas decimais
    return accuracy, precision

# Create a function to find the matrix index with the best combined accuracy and precision
def best_performance(matrices):
    best_index = 0
    best_accuracy = 0
    best_precision = 0

    # Loop through each matrix to calculate metrics
    for index, matrix in enumerate(matrices):
        tp, fp, fn, tn = map(int, matrix)
        
        # Calculate accuracy and precision
        accuracy, precision = calculate_metrics(tp, fp, fn, tn)

        # Update best metrics if found
        if accuracy + precision > best_accuracy + best_precision:
            best_index = index + 1
            best_accuracy = accuracy
            best_precision = precision
            
    return best_index, best_accuracy, best_precision

# Print the results without formatting
index1, accuracy1, precision1 = best_performance([[50,10,5,85], [20,5,8,67], [30,12,4,88]])
print("Índice:", index1)
print("Acurácia:", accuracy1)
print("Precisão:", precision1)

index2, accuracy2, precision2 = best_performance([[70,15,8,78], [60,20,10,80], [45,5,3,92], [80,7,15,98]])
print("Índice:", index2)
print("Acurácia:", accuracy2)
print("Precisão:", precision2)

index3, accuracy3, precision3 = best_performance([[100,0,0,50], [80,10,2,98]])
print("Índice:", index3)
print("Precisão:", precision3)