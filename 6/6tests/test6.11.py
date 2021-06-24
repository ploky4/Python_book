# This program build html file with
# data of user

def main():
    # Get data from user
    name = input('Введите своё имя: ')
    descr = input('Опишите себя: ')

    # Create new files user.html
    user_file = open('name.html', 'w')

    # Write data into the new file
    user_file.write('<html>' + '\n')
    user_file.write('<head>' + '\n')
    user_file.write('</head>' + '\n')
    user_file.write('<body>' + '\n')
    user_file.write('\t' + '<center>' + '\n')
    user_file.write('\t' + '<h1>' + name + '</h1>' + '\n')
    user_file.write('\t' + '<center>' + '\n')
    user_file.write('\t' + '<hr />' + '\n')
    user_file.write('\t' + descr + '\n')
    user_file.write('\t' + '<hr />' + '\n')
    user_file.write('</body>' + '\n')
    user_file.write('</html>' + '\n')

    # Print task complete
    print('Data added to the file')

    # Close the file
    user_file.close()


# Use main function
main()
