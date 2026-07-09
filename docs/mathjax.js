window.MathJax = {
    tex: {
        inlineMath: [["\\(", "\\)"], ["$", "$"]],
        displayMath: [["\\[", "\\]"], ["$$", "$$"]],
        processEscapes: true,
        processEnvironments: true,
        macros: {
            R: "{\\mathbb{R}}",
            C: "{\\mathbb{C}}",
            ppp: "{\\mathbb{ppp}}",
        }
    },
    options: {
        ignoreHtmlClass: ".*",
        processHtmlClass: "arithmatex"
    }
};