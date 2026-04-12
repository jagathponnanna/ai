from generate import generate_seats, generate_passengers
from allocation import hybrid_allocate


def generate_html(seats, filename="seatmap.html"):

    html = """
    <html>
    <head>
    <style>
    body { font-family: Arial; background:#0f172a; color:white; }
    .row { display:flex; margin:5px; justify-content:center; }
    .seat { width:60px; height:60px; margin:3px;
            background:#1e293b; border-radius:8px;
            text-align:center; font-size:10px; padding:5px;}
    .occupied { background:#2563eb; }
    .exit { background:#16a34a; }
    .aisle { width:30px; }
    </style>
    </head>
    <body>
    <h2 align="center">A320 Seat Map</h2>
    """

    # group seats by row
    rows = {}
    for s in seats.values():
        rows.setdefault(s.row, []).append(s)

    for r in sorted(rows.keys()):
        html += '<div class="row">'

        row_seats = sorted(rows[r], key=lambda x: x.col)

        for i, s in enumerate(row_seats):

            if i == 3:
                html += '<div class="aisle"></div>'

            cls = "seat"
            if s.passenger:
                cls += " occupied"
            if s.is_exit:
                cls += " exit"

            html += f'<div class="{cls}">'
            html += f"{s.seatid}<br>"

            if s.passenger:
                html += f"{s.passenger.pid}<br>{s.passenger.loyalty}<br>{s.passenger.prefers}<br> {s.passenger.paid_seat} "

            html += "</div>"

        html += "</div>"

    html += "</body></html>"

    with open(filename, "w") as f:
        f.write(html)



def main():
    seats = generate_seats()
    passengers = generate_passengers()
    hybrid_allocate(passengers, seats)
    generate_html(seats)
    print("Seatmap.html generated!")


if __name__ == "__main__":
    main()