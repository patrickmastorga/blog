window.MathJax = {
    tex: {
        inlineMath: [["\\(", "\\)"], ["$", "$"]],
        displayMath: [["\\[", "\\]"], ["$$", "$$"]],
        processEscapes: true,
        processEnvironments: true,
        macros: {
            R: "{\\mathbb{R}}",
            C: "{\\mathbb{C}}",
        }
    },
    options: {
        ignoreHtmlClass: ".*",
        processHtmlClass: "arithmatex"
    }
};