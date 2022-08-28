<template>
    <div>
        <!-- <H1>Exemplo Simples</H1> -->
        <Plotly :data="data" :layout="layout" :display-mode-bar="false"></Plotly>
    </div>
</template>

<script>
export default {
  data() {
    return {
      data: [
        {
          x: [1, 2, 3, 4],
          y: [10, 15, 13, 17],
          type: "scatter",
        },
      ],
      layout: {
        title: "My graph",
      },
    };
  },
};
</script>

<style>
</style>