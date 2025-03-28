def render_multiline_text(text, font, surface, x, y, colour, wobble=False):
        lines = text.split('\n') # manual spacing, just add \n within the string. This could be improved by length and ' '
        char_width = 8 # would need to be changed or made dynamic if font was a different size than what I used
        line_height = 8 # would need to be changed or made dynamic if font was a different size than what I used

        if wobble: # makes each character wobble up and down
            for i, line in enumerate(lines):
                for j, char in enumerate(line):
                    w = random.randint(-1,1) # amount of wobble
                    text_surface = font.render(char, True, colour)
                    surface.blit(text_surface, (x + j * char_width, y + w + i * line_height))

        else:
            for i, line in enumerate(lines):
                text_surface = font.render(line, True, colour)
                surface.blit(text_surface, (x, y + i * line_height))