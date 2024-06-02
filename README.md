# abg
this stands for _**a**scii-**b**ased **g**raphics format._ this is an ideal file format for terminal-based graphics.

## example
here's abg in action:
```
a person waving hello
xx xx xx xx xx xx xx xx
xx xx y4 y4 y4 xx xx xx
xx y4 w4 w4 w4 y4 xx xx
y2 w4 w4 w4 w4 w4 y4 xx
y2 w4 w1 w4 w1 w4 y4 xx
y2 w4 w4 w4 w4 w4 y4 xx
y2 w1 w4 w4 w4 w1 y4 xx
y2 y2 w1 w1 w1 y4 y4 xx
y2 y2 y2 w1 y4 y4 xx w1
xx y2 w1 w1 w1 y4 w1 xx
xx w1 y2 w1 y2 w1 xx xx
xx w1 xx w1 xx xx xx xx
xx w1 xx w1 xx xx xx xx
xx xx xx w1 xx xx xx xx
xx xx w1 xx w1 xx xx xx
xx xx w1 xx w1 xx xx xx
xx xx w1 xx w1 xx xx xx
xx xx w1 xx w1 xx xx xx
xx xx w1 xx w1 xx xx xx
xx w1 w1 xx w1 w1 xx xx
```
becomes

![image](https://github.com/qwertyy-dev/abg/assets/129226914/ca8a21e5-35dd-4817-bd69-9a05d065f2da)

## limitations
yes, there are limitations. only **20** different colors are supported (three shades of red, yellow, green, blue, purple, white, along with black and a transparent option)
however, this is still an optimal option for terminal-based graphics.

## how to make a `.abg` file
the first line does nothing. you can do whatever you want with it. from that point forward, it starts reading for pixels. here is how a pixel is transformed:
- the first letter is the color.
  - `r` = red
  - `y` = yellow
  - `g` = green
  - `b` = blue
  - `c` = cyan
  - `p` = purple
  - `w` = white
  - `x` = transparent
- the second letter is the brightness.
  - `1` = black
  - `2` = very dark
  - `3` = little darker
  - `4` = bright
  - `x` = transparent
