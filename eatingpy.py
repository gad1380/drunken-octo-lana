#This line replaces the formatted variable with 10
x = "There are %d types of people." % 10
#Assigns binary to binary
binary = "binary"
#assigns do not to dont
do_not = "don't"
#replaces two formatted variables with two values, which need to be in parenthesis
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

#prints a string with a formated variable of another string
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False

joke_evaluation = "Isn't that joke so funny?! %r"

#prints a strings with a boolean value inside the formatted variable
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
