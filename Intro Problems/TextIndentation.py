""" Write a program to remove the endline from a string/paragraph """
string = "This is a test string \n"
print(string)
print(string)
print(string.rstrip())
print(string.rstrip())
#removing the endline character
""" Checking if a string starts with a character """
string1 = "Mario"
print(string1.startswith("M"))
""" Display formatted text (width = 50) """
import textwrap

sampleText = ''' 
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java
'''
widthFormatted = textwrap.fill(sampleText, width = 50)
print(widthFormatted)
deindentedText = textwrap.dedent(sampleText)
print(deindentedText)

""" indent to ad indentation to paragrap, can specify if blank or not"""
finalResults = textwrap.indent(deindentedText, '<<')
print()
print(finalResults)

""" .strip() removes all leading and trailing blanks """
newstring = ''' 
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java
'''
print(newstring)
print()
text2 = textwrap.dedent(newstring).strip()
print(text2)
print()
print(textwrap.fill(text2,initial_indent = '', subsequent_indent = ' '*4, width = 80))
print()
x = 3.1415926
y = 12.999999
print("\nOriginal Number: ", x)
print("Formatted Number: " + "{:.2f}".format(x))
print("\nOriginal Number: ", y)
print("Formatted Number: " + "{:.2f}".format(y))
print("\nOriginal Number", x)
print("Formatted Number: " + "{:.3f}".format(x))
print("\nOriginal Number: ", y)
print("Formatted Number: " + "{:.4f}".format(y))

""" Adding signs to formatted numbers """
print("\nOriginal Number: ", x)
print("Formatted Number: "+"{:+.2f}".format(x))
print("\nOriginal Number: ", y)
print("Formatted Number: "+"{:+.3f}".format(y))

""" adding zeros before an integer """
xx = 3
yy = 123
print("\nOriginal Number: ", xx)
print("Formatted Number(left padding, width 2): " + "{:0>2d}".format(xx))
print("\nOriginal Number: ", yy)
print("Formatted Number(left padding, width 6):" + "{:0>6d}".format(yy))

""" adding commas to numbers (more than 3 digits)"""
xxx = 3000
yyy = 3000000000
print("\nOriginal Number: ",xxx)
print("Formatted Number(commas):"+"{:,}".format(xxx))
print("\nOriginal Number: ", yyy)
print("Formatted Number: "+"{:,}".format(yyy))

""" Format Number as Percentage """
xX = .03
xY = .07

print("\nOriginal Number: ", xX)
print("Formatted number as percentage: " + "{:.2%}".format(xX))
print("\nOriginal Number: ", xY)
print("Formatted number as percentage: " + "{:.2%}".format(xY) )

""" Aligning a string to the right/left/centered """
mar = 23
print("\nOriginal Number: ", mar)
print("Left Aligned (width 10): "+"{:<10d}".format(mar))
print("Right Aligned (width 10): "+"{:10d}".format(mar))
print("Center Aligned (width 10): "+"{:^10d}".format(mar))



