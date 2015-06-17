---
layout: post
title: First shapes in D3
tags: python
summary: I have began learning D3. Having spent some considerable time I have come to realize that D3 has a steep learning curve. 
---
I have began learning D3. Having spent some considerable time I have come to realize that D3 has a steep learning curve. I have attempted to learn D3 over 10 times and every time I have given up. However, the vector graphics, the amazing interactive visualization, and the sheer creativity that D3 provides draws me to it. Nonetheless, today I celebrate a small victory as I have been successful in creating "shapes" in D3. This first graphic will go towards my project Mining the NASA Database. Nonetheless, I have excited to show you the graphics and the code. So, without losing any time, here's what I have:

The end result is the following: 
![My helpful screenshot](/assets/first_shapes.png)


{% highlight javascript %}

var margin = {top: 30, right: 20, bottom: 30, left: 50},
            width = 800 - margin.left - margin.right,
            height = 670 - margin.top - margin.bottom;

            // Define the array of two circles
            var jsonCircles = [
            {"x_axis": 450, "y_axis": 350, "radius": 200, "strokeColor": "white", "strWidth": 3 ,"fill": "#9a9a9a"},
            {"x_axis": 550, "y_axis": 350, "radius": 100, "strokeColor": "white", "strWidth": 3 ,"fill": "#9a9a9a"},
            ]

            // Adds the svg canvas
            var svg = d3.select("body")
                        .append("svg")
                        .attr("width", width + margin.left + margin.right)
                        .attr("height", height + margin.top + margin.bottom)
                        .append("g")
                        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

            var circles = svg.selectAll("circle")
                             .data(jsonCircles)
                             .enter()
                             .append("circle");

            var circleAttributes = circles
                        .attr("cx", function(d) {return d.x_axis;})
                        .attr("cy", function(d) {return d.y_axis;})
                        .attr("r", function(d) {return d.radius;})
                        .style("stroke", function(d) {return d.strokeColor;})
                        .style("stroke-width", function(d) {return d.strWidth;})
                        .style("fill", function(d) {return d.fill;});

{% endhighlight javascript %}

That's all. I hope you will find this helpful. In the meanwhile I will proceed to my next goal, creating a scatterplot of 180,000 points in D3