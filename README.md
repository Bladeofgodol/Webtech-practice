# Webtech-practice
This are all the practice codes ive written for my webtech class at ACT
since all of the codes contain comments i haven't written them in this read me
HTML:

    most html tags begin with <tagname> and end with</tagname>
    html: main html tag
    head: to store meta data
    title: the title to be displayed in tab bar
    body: the main element of the page
    a href="link.html": to link to another page
    p: tag to write paragraphs
    ol: tag for ordered list
    li: a tag for the list item
    table: tag for table
    tr: Table row
    td: tag for table item
    h1: tag for heading type 1
    nav: defines a set of navigation links
    aside:  defines some content aside from the content it is placed in (like a sidebar)
    time: to specify date and time
    meta: Defines metadata about an HTML document
    output: Defines the result of a calculation
    img src="": define an image and its source
    code: Defines a piece of computer code
    embed: define container for an external application
    video: define an embeded video content
    var: define a variable
    form action="https://www.google.com/search" method="get": tag for creating new form to indicated link
    input type="search" name="": search bar
    input type="submit" value="search" target="_blank": excute button
CSS:

    link rel="stylesheet" href="style.css": for external css in same folder as html file
    style: for internal css
        we can refer to internal css by using class="class_name"
    - for inline css we can use style="attribute:value;"
    header: to specify header
    main: to specify main part of the body
    footer: to specify footer part of the body
    div: to create a specfic container
           - we can create a container within a container
    color: is a changeable attribute of an element
    hover: a class property where it is activated when cursore is hovered on element using the class
    - we can specify what element is changed by specifiying in in the style tag
    flex: a value of display allowing the internals to change with size
    wrap: a value of flex-wrap that allow horizontal items to wrap into vertical
    @media: to change attribute value at certain conditions of the display


    BOOTSTRAP:
        a framework for web design
        <link href="Secondpractice/bootstrap/css/bootstrap.css "rel="stylesheet">: import of the bootstrap css file type
        <script src="/Secondpractice/bootstrap/js/bootstrap.bundle.min.js" ></script>: optional import the bootstrap js file type
        - we refer to bootstrap attributes by using class=""

JS:
    onload="": page loading listener
    onclick="": button with inline js click listener
    onmouseover="alert ('you put your cursor over it')": inline js cursor over listener and alert
    onkeydown="": keyboard input listner
    script: internal JS tag
        var link = document.getElementById("mylink"): select elemnts by attribute id
        var herf = link.getAttribute("href"): getting the attribute by value
        var y = 10;//variables to store any type of value ie:int,bool,char...
        var sum = x + y;//basic arithmetics
        document.write(sum);//js output

        /* multiline comments
        are written like this */

        let z = 43; //let is a new type of var
        -js is case sensetive
        //let new = "wow"; //error because new is a "reserved" keyword
        


Python:
    print("") # print the output
    name = input('words to display') #to input by users 
    print('yourname is: \n' + name) #use + for concationation 
    print(f'yourname is: {name}') #f string lets u format ur datatype
    number = 89 #stores litrals(values) without needing specifying datatypes
    float_number = 69.0 # this variable naming  method is called snake method by using underscores
    print(type(float_number)) #displays the datatype of the variable
    - keywords are reserved words that cant be variable name
    if age >= 18:  # if else computation
        #then do something
    else: #else
        #do something else
         pass #simply leaves the condtion
    def example(parameter:str, arg:int): #defining a function and converting global variable to local
    list_of_numbers = [1,2,3,4,3,4,56,7,8,9,0] #listing an ordered sequence of items with diffrent and can be modified(muttable) datatype using []
    print(len(list_of_numbers)) #prints length of the list
    print(list_of_numbers[]) #print the value of specified index in the list
    print(list_of_numbers[a:b]) #print in range from a to b
    list_of_numbers.sort() #sorts the elemets of a list
    list_of_numbers.append(23) #add new element at end
    list_of_numbers[4] = 5 #change the value of an index spacified
    tuple_of_numbers = (1,2,3,4,5,6) # same as listing but tuple elements cant be modified
    set_of_stuff = {1,23,4,5,'words'} #set stores unique values, not limited with one datatype at a time
    number_dictionary = {'name':'jer','age':21,'gender':' helicopter'} #it stores unordered collecton of key and values


