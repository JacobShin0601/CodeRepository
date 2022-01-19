

def average_of_inputs(inputs):
    result = sum(inputs)/len(inputs)
    return result

def comparison_of_input_and_average(average, inputs_list):
    greater_item_list = []

    for item in inputs_list:
        if (item > average):
            greater_item_list.append(item)
    
    return greater_item_list

def main():
    inputs_list = []
    input_stop_tag = False

    while(input_stop_tag==False):
        input_item = input("Please enter the score: ")
        if (input_item == 'done'):
            input_stop_tag = True
        else :
            input_item = float(input_item)
            inputs_list.append(input_item)
    
    result_average_of_result = average_of_inputs(inputs_list)
    print("Average score is", result_average_of_result)

    greater_list = []
    greater_list = comparison_of_input_and_average(result_average_of_result, inputs_list)

    print("The greater item than average is ")
    for item in greater_list:
        print(item)

main()

