# acsii-based graphics format

file = open(input("open a file... "), "r")

class abg:
	def interpret(file):
		try:
			lines = file.read().splitlines()

			if file.name.lower().endswith(".abg"):
				brightnesslevels = ["1", "2", "3", "4", "x"]
				brightness = ["  ", "░░", "▓▓", "██", "\033[0m  \033[40m"]
				colornames = ["r", "g", "y", "c", "p", "b", "w", "x"]
				colors = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m", "\033[37m", ""]
				result = "\033[40m"
				for y in range(len(lines)-1):
					linepixels = lines[y+1].split(" ")
					for x in range(len(linepixels)):
						pixel = linepixels[x]
						if pixel[0].lower() in colornames:
							result += colors[colornames.index(pixel[0].lower())]
							if pixel[1].lower() in brightnesslevels:
								result += brightness[brightnesslevels.index(pixel[1].lower())]
							else:
								return "invalid brightness level"
						else:
							return "invalid color"
					result += "\n"
				return result
			else:
				return "this is not a .abg file"
		except AttributeError:
			return "something went wrong!"

print(abg.interpret(file))
