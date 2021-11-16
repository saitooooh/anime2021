studio = AStudio()
shape = RollingPolygon(width=200, N=10)
studio.append(shape)
studio.append(AImage(width=100, image='cat_exotic_shorthair.png'))
for i in range(200):
  studio.render()
IPython.display.Image(studio.create_anime())
