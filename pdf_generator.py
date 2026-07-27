from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import lightgrey, Color
from datetime import datetime
import os



# ======================
# 中文字型
# ======================

font_path = "fonts/kaiu.ttf"


pdfmetrics.registerFont(
    TTFont(
        "KaiTi",
        font_path
    )
)



# ======================
# PDF產生
# ======================

def generate_pdf(text, cols, style):


    os.makedirs(
        "output",
        exist_ok=True
    )



    # Noteful適合檔名
    date = datetime.now().strftime("%Y%m%d")


    filename = os.path.abspath(
        f"output/練字字帖_{date}.pdf"
    )



    pdf = canvas.Canvas(
        filename,
        pagesize=A4
    )



    width, height = A4



    # ======================
    # A4版面設定
    # ======================


    margin = 45

    top_margin = 100

    bottom_margin = 60


    gap = 8



    size = (

        width
        - margin * 2
        - gap * (cols-1)

    ) / cols



    font_size = size * 0.65



    rows_per_page = int(

        (

            height
            - top_margin
            - bottom_margin

        )
        /
        (size + gap)

    )



    x_start = margin



    index = 0



    total = len(text)



    # ======================
    # 每頁處理
    # ======================

    while index < total:


        y_start = height - top_margin



        pdf.setFont(
            "KaiTi",
            font_size

        )



        pdf.setFillColor(

            Color(
                0.75,
                0.75,
                0.75
            )

        )



        for row in range(rows_per_page):


            for col in range(cols):


                if index >= total:

                    break



                char = text[index]



                x = (

                    x_start
                    +
                    col*(size+gap)

                )


                y = (

                    y_start
                    -
                    row*(size+gap)

                )



                draw_cell(

                    pdf,

                    x,

                    y,

                    size,

                    style,

                    char,

                    font_size

                )



                index += 1



        # 還有文字才換下一頁

        if index < total:

            pdf.showPage()



    pdf.save()



    return filename





# ======================
# 畫單一格
# ======================

def draw_cell(pdf, x, y, size, style, char, font_size):


    pdf.setStrokeColor(
        lightgrey
    )



    # 空白格

    if style != "blank":


        pdf.rect(

            x,

            y,

            size,

            size

        )



    # 田字

    if style in [
        "tian",
        "mi"
    ]:


        pdf.line(

            x,

            y+size/2,

            x+size,

            y+size/2

        )


        pdf.line(

            x+size/2,

            y,

            x+size/2,

            y+size

        )



    # 米字

    if style == "mi":


        pdf.line(

            x,

            y,

            x+size,

            y+size

        )


        pdf.line(

            x,

            y+size,

            x+size,

            y

        )



    # 九宮格

    if style == "jiu":


        pdf.line(

            x+size/3,

            y,

            x+size/3,

            y+size

        )


        pdf.line(

            x+size*2/3,

            y,

            x+size*2/3,

            y+size

        )


        pdf.line(

            x,

            y+size/3,

            x+size,

            y+size/3

        )


        pdf.line(

            x,

            y+size*2/3,

            x+size,

            y+size*2/3

        )



    # 描紅字

    pdf.drawCentredString(

        x + size/2,

        y + size/2 - font_size*0.35,

        char

    )