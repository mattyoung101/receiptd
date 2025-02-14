// Colour links blue like LaTeX
#show cite: set text(fill: blue)
#show link: set text(fill: blue)
#show ref: set text(fill: blue)
#show footnote: set text(fill: blue)
// Font size
#set text(size: 14pt, font: "Hack Nerd Font")
#show raw: set text(size: 8pt)
// Display
#set page(
    width: 80mm,
    height: 297mm,
    margin: (
        left: 5mm,
        right: 5mm,
        top: 5mm,
        bottom: 5mm
    )
)
#set par(justify: true)

#align(center, [
= BACKGROUND JOB \ COMPLETED
])

#line(length: 100%)

#set text(size: 12pt)
*JOB:* #sys.inputs.name

*TIME:* #sys.inputs.time

*STATUS:* #sys.inputs.status

*LOG:*

#raw(sys.inputs.log)

#v(2em)

#set text(size: 8pt)
SERVED BY: MAINFRAME "#sys.inputs.hostname" ON _#sys.inputs.hostname\.LOCAL_

(C) #datetime.today().year() CONTROL DATA CORPORATION
