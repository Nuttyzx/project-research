<template lang="">
    <div>
      <div id="graph"></div>
    </div>
  </template>
  <script>
  import * as d3 from "d3";
  
  export default {
    data() {
      return {
        nodes: [
          {
            id: "Structural basis of PROTAC cooperative recognition for selective protein degradation.",
            group: "Cited Works",
            radius: 2,
            citing_patents_count: 2,
          },
          {
            id: "The influence of rough lipopolysaccharide structure on molecular interactions with mammalian antimicrobial peptides",
            group: "Cited Works",
            radius: 1,
            citing_patents_count: 1,
          },
          {
            id: "New Synthetic Routes to Triazolo-benzodiazepine Analogues: Expanding the Scope of the Bump-and-Hole Approach for Selective Bromo and Extra-Terminal (BET) Bromodomain Inhibition.",
            group: "Cited Works",
            radius: 1,
            citing_patents_count: 1,
          },
          {
            id: "109-294-662-661-65X",
            group: "Citing Patents",
          },
        ],
        links: [
          {
            source:
              "Structural basis of PROTAC cooperative recognition for selective protein degradation.",
            target: "109-294-662-661-65X",
            value: 2,
          },
        ],
      };
    },
    mounted() {
      // เรียกใช้ฟังก์ชันสร้างกราฟเมื่อคอมโพเนนต์ถูกเปิดใช้งาน
      this.createGraph();
      console.log(this.nodes)
      console.log(this.links);
    },
    methods: {
      createGraph() {
        // ระบุขนาดของกราฟ
        const width = 600;
        const height = 400;
        const color = d3.scaleOrdinal(d3.schemeCategory10);
        // สร้าง SVG container สำหรับกราฟ
        const svg = d3
          .select("#graph")
          .append("svg")
          .attr("height", height)
          .attr("viewBox", [-width / 2, -height / 2, width, height])
          .attr("style", "max-width: 100%; height: auto;");
  
        // สร้าง force simulation
        const simulation = d3
          .forceSimulation(this.nodes)
          .force(
            "link",
            d3.forceLink(this.links).id((d) => d.id)
          )
          .force("charge", d3.forceManyBody())
          .force("x", d3.forceX())
          .force("y", d3.forceY());
  
        // สร้างเส้นเชื่อม
        const link = svg
          .append("g")
          .attr("stroke", "#999")
          .attr("stroke-opacity", 0.6)
          .selectAll("line")
          .data(this.links)
          .join("line")
          .attr("stroke-width", (d) => Math.sqrt(d.value));
  
        // สร้างโหนด
        const node = svg
          .append("g")
          .attr("stroke", "#fff")
          .attr("stroke-width", 1.5)
          .selectAll("circle")
          .data(this.nodes)
          .join("circle")
          .attr("r", 5)
          .attr("fill", (d) => color(d.group));
  
        // เพิ่ม title สำหรับโหนด
        node.append("title").text((d) => d.id);
  
        node.call(
          d3
            .drag()
            .on("start", dragstarted)
            .on("drag", dragged)
            .on("end", dragended)
        );
  
        // ทำให้โหนดและเส้นเชื่อมมีการอัพเดทตำแหน่งเมื่อกราฟเคลื่อนไหว
        simulation.on("tick", () => {
          link
            .attr("x1", (d) => d.source.x)
            .attr("y1", (d) => d.source.y)
            .attr("x2", (d) => d.target.x)
            .attr("y2", (d) => d.target.y);
  
          node.attr("cx", (d) => d.x).attr("cy", (d) => d.y);
        });
  
        function dragstarted(event) {
          if (!event.active) simulation.alphaTarget(0.3).restart();
          event.subject.fx = event.subject.x;
          event.subject.fy = event.subject.y;
        }
  
        // Update the subject (dragged node) position during drag.
        function dragged(event) {
          event.subject.fx = event.x;
          event.subject.fy = event.y;
        }
  
        // Restore the target alpha so the simulation cools after dragging ends.
        // Unfix the subject position now that it’s no longer being dragged.
        function dragended(event) {
          if (!event.active) simulation.alphaTarget(0);
          event.subject.fx = null;
          event.subject.fy = null;
        }
        simulation.on("end", () => console.log("Simulation ended."));
  
        return svg.node();
      },
    },
  };
  </script>
  <style lang=""></style>
  