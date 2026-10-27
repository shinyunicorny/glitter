weather = input("what the weather like? ")
temperature = input("is it cold outside? ")
temperaturesness = int(input("what's the approximate temperature? "))

if weather in ["foggy", "fog"]:
    print("just like in silent hill...")
    
elif weather in ["rainy", "rain"]:
    print("tap-tap-tap")
    
elif weather in ["snowy", "snow"]:
    print("lucky you. i would like to see snow someday...")
    
else:
    print("strange, seemed it was something else...")

if temperature in ["yes", "cold", "i'm shaking"]:
    
    if temperaturesness <= 7:
        print("you can buy hot chocolate, then? it's actually freezing.")
        
    else:
        print("wait, you said you're cold, but it's", temperaturesness, "degrees?")
        print("are you sure you don't have a fever?")
        
elif temperature in ["no", "warm", "hot"]:
    
    if temperaturesness >= 15:
        print("my hands are literally shaking, it's definitely not warm there.")
        
    else:
        print("you said it's warm, but it's only", temperaturesness, "degrees...")
        
        print("you sure you don't have a frostbite? ")
        
else:
    print("shit, seems like the line went dead...")
    print("call me later, alright?")