
var div = undefined;
window.onload = () => {
    console.log('hello')
    div = d3.selectAll("div");
    console.log(div)
    d3.select(".playground-container").append("svg")
}
