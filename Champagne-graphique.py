# projet pour traiter les donnes les donnees des clients et ensuite les demontrer
# en graphique pour que le vigneron sache les habitudes d'achat du client

""" Project that displays clients' previous purchases so that the business owner 
can better understand their purchase habits
***Note: expected outputs are based off of CSV file
Example Outputs

customer_purchases();
Victoria
>>>le nombre total de bouteilles est 72
Other available names: Frank, Laura
"""


import matplotlib.pyplot as plt
import numpy as np


def customer_purchases():

    # FUNCTIONS
    # function to calculate number of bottles

    def calc_num_bottles(my_string, num_bottles):
        # B = standard bottle, 75cl
        if my_string[0] == 'B':
            short_product = 1 * int(num_bottles)
        # M = double bottle 150 cl
        elif my_string[0] == 'M':
            short_product = 2 * int(num_bottles)
        # D = half a bottle
        elif my_string[0] == 'D':
            short_product = 0.5 * int(num_bottles)
        return short_product

    # RETREIVING DATA FROM CSV FILE
    client_list = []
    in_file = open('sample-data-v3.csv', 'r')
    header = True

    for line in in_file:
        line = line.strip()
        line = line.split(',')

        if header:
            header = False
        else:
            info_tuple = (line[0], line[1], line[2], line[3])
            # print('hello')
            client_list.append(info_tuple)

    #print("client information:", client_list)
    # error checking
    check = True
    while check:
        client_name = input(
            'Entrez le nom du client dont vous souhaitez recuperer les informations \n')

        # list used for storing information that will be graphed
        temp_list = []

        counter = 0
        # retreive required information
        # iterate through the client list
        for tup in client_list:
            # if the client name is the required one
            if client_name in tup[0]:
                temp_list.append(tup)
                counter += 1
        # check to see if the clients name entered is in the database
        if counter != 0:
            check = False
        else:
            print(
                'Ce nom n\'existe pas dans notre systeme. Veuillez entrez un autre nom')
    # PLOT GRAPH
    graph_list = []

    for i in range(len(temp_list)):
        # find information about the bottles
        found = False
        key_list = list()
        for j in range(len(graph_list)):
            key_list = list(graph_list[j].keys())

            if temp_list[i][1] == key_list[0]:

                my_values = graph_list[j].get(key_list[0])
                #print("value", my_values)
                # append the new values with the same date to the list of original values
                my_values.append((temp_list[i][2], temp_list[i][3]))
                found = True

        if found == False:
            graph_list.append(
                {temp_list[i][1]: [(temp_list[i][2], temp_list[i][3])]})
            Found = True

    # last sort

    # for cuvee BBE
    y_bbe = []
    count_bbe = 0

    # for cuvee BDE
    y_bde = []
    count_bde = 0
    # for cuvee BRO
    y_bro = []
    count_bro = 0

    # for cuvee BSG
    y_bsg = []
    count_bsg = 0

    # for cuvee BDY
    y_bdy = []
    count_bdy = 0

    x_range = []
    new_list = []

    for i in range(len(graph_list)):
        # print(graph_list[i])
        purchase_per_date = list(graph_list[i].values())
        x_range += list(graph_list[i].keys())
        #print('purchase:', purchase_per_date)

        for j in range(len(purchase_per_date)):
            #print('in:', purchase_per_date)
            for lis in purchase_per_date:
                # for each separate order, append to a new list
                for tup in lis:
                    if tup[0] == 'BBE':
                        y_bbe.append(int(tup[1]))
                        count_bbe += 1
                    elif tup[0] == 'BDE':
                        y_bde.append(int(tup[1]))
                        count_bde += 1
                    elif tup[0] == 'BRO':
                        y_bro.append(int(tup[1]))
                        count_bro += 1
                    elif tup[0] == 'BSG':
                        y_bsg.append(int(tup[1]))
                        count_bsg += 1
                    elif tup[0] == 'BDY':
                        y_bdy.append(int(tup[1]))
                        count_bdy += 1
                # if there wasn't an option for that purchase, to keep the same
                # length of list for all cuvees
                if count_bbe == 0:
                    y_bbe.append(0)
                if count_bde == 0:
                    y_bde.append(0)
                if count_bro == 0:
                    y_bro.append(0)
                if count_bsg == 0:
                    y_bsg.append(0)
                if count_bdy == 0:
                    y_bdy.append(0)

                # set count back to zero
                count_bbe = 0
                count_bde = 0
                count_bro = 0
                count_bsg = 0
                count_bdy = 0

    fig1 = plt.figure()

    plt.title('Quantite de cuvee vendu par date')
    plt.xlabel = ('les dates')
    plt.ylabel = ('nombre de chaque cuvee')
    plt.plot(x_range, y_bbe, 'y+', label='BBE')
    plt.plot(x_range, y_bde, 'b+', label='BDE')
    plt.plot(x_range, y_bsg, 'c+', label='BSG')
    plt.plot(x_range, y_bdy, 'g+', label='BDY')
    plt.plot(x_range, y_bro, 'm+', label='BRO')

    plt.legend(loc="upper left")
    plt.show()

    # TOTAL NUMBER OF BOTTLES
    total_bottles = 0
    for i in range(len(temp_list)):
        my_string = temp_list[i][2]
        num_bottles = temp_list[i][3]
        total_bottles += calc_num_bottles(my_string, num_bottles)
    print('le nombre total de bouteilles est', total_bottles)

    # PIE CHART
    y_list = []
    my_labels = []

    # retrieve information
    for i in range(len(temp_list)):
        # need to sort the values
        if temp_list[i][2] not in my_labels:
            y_list.append(int(temp_list[i][3]))
            my_labels.append(temp_list[i][2])
        else:
            for j in range(len(my_labels)):
                if temp_list[i][2] == my_labels[j]:
                    y_list[j] += int(temp_list[i][3])

    fig2 = plt.figure()
    plt.title("pourcentage de chaque cuvee vendu a " + temp_list[0][0] + " depuis "
              + temp_list[-1][1])
    y = np.array(y_list)
    # autopct displays percentages on pie chart
    plt.pie(y, labels=my_labels, autopct='%.2f%%')

