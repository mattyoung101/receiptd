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
        left: 0mm,
        right: 0mm,
        top: 0mm,
        bottom: 0mm
    )
)
#set par(justify: true)

#align(center, [
= BACKGROUND JOB \ COMPLETED
])

// #line(length: 100%)

#image("separator.svg")

#set text(size: 12pt)
*JOB: #sys.inputs.name*

*TIME: #sys.inputs.time*

*STATUS: #sys.inputs.status*

// *LOG:*
//
// #raw(sys.inputs.log)

#v(2em)

#set text(size: 10pt)
*SERVED BY:*

*MAINFRAME "#sys.inputs.hostname" ON _#sys.inputs.hostname\.LOCAL_*

(C) #datetime.today().year() DATA CONTROL CORPORATION


#align(center, [
    #image("norecycle.svg", width: 15%)

    _CANNOT BE RECYCLED_
])
