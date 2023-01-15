#Nick Dang
#101286968
#Description: a program to perform "magic phone number" by doing complex calculation to the 
#phone # while still producing the same result.

phoneNumber= int(input("Your phone #: "))

prefix= phoneNumber//10000
suffix= phoneNumber%10000

firstPrefixResult= prefix*80
secondPrefixResult= (firstPrefixResult+1)*250

firstSuffixResult= 2*suffix + secondPrefixResult
secondSuffixResult= (firstSuffixResult - 250)/2

print("Your prefix is ",prefix,". Multiply this by 80, and the result is: ",firstPrefixResult,
"\nAdd 1 to that result and multiply it by 250, and the result is: ", secondPrefixResult,
"\nYour line number is ",suffix,". Add this to the previous result twice, and the result is: ",firstSuffixResult,
"\nSubtract 250 from that result and divide it by 2, and the result is: ", int(secondSuffixResult))



