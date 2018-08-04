import pandas as pd
import os

def main():
    df = pd.read_csv("./bptms_Employed_persons_by_educational_attainment_state-1.csv")

    if not os.path.exists("image_dir"):
        os.makedirs("image_dir")

    for s in df["State/Country"].unique():
        plot = draw_chart(df, s)
        figure = plot.get_figure()
        figure.savefig("image_dir/" + s+".png")

def draw_chart(df, state):
    df_state = df[df["State/Country"] == state]
    df_year = df_state.pivot(index="Year", columns="Educational attainment", values=" Employed Person ('000) ")
    df_year = df_year.convert_objects(convert_numeric=True)
    title = "{state} employee in (,000)".format(state=state)
    plot = df_year.drop(["Total"],axis=1).plot.area(title=title, )
    return plot

if __name__ == "__main__":
    main()