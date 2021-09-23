import plotly.express as px

x = ["a","b","c"]
y = [1,2,3]
fig = px.line(x, y, title="sample figure")
# print(fig)
# fig.show()

fig.write_image("images/fig2.png")