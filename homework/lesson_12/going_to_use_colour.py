from colour_for_lesson import mcolour as mc


print(mc.error_message("the best code I ever used"))
print(
    mc.color_text("Give me the colour", '33m')
)

for num, colour_key in enumerate(mc.colour):

    init_text =  mc.color_text("Now it is a text", mc.colour['red'])

    key_coloured = mc.color_text( colour_key, mc.colour.get(colour_key))

    print(
        f"{num:>2}. {init_text} :  {key_coloured}"
    )

