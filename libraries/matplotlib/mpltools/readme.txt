
mpltools
  - provides tools for Matplotlib that make it easier to adjust the style,
    choose colors, make specialized plots, etc.
  - is a great library for making beautiful ggplot-like (from R) charts in
    Python. 


Predefined styles
   located in mpltools/style/
   for example ggplot (emulates the aesthetics of ggplot)


from mpltools import style
style.use('ggplot')


List available styles:
   print(style.available)


mplstyle file  (~/.mplstylelib/)


   [style1]
   
   text.fontsize = 12
   figure.dpi = 150
   
   [style2]
   
   text.fontsize = 10
   font.family = 'serif'

Priority of style files:
  •    ./mplstyle
  •    ~/.mplstyle
  •    ~/.mplstylelib/*.rc
  •    mpltools/style/*.rc

The plot2rst Sphinx extension provides a simple way to generate reStructuredText (rst) examples from python files.
