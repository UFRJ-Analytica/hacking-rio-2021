

<template>

    <Plotly :data="data" :layout="layout" :display-mode-bar="false"></Plotly>
 
</template>

<script>
export default {
  props: ["uc"],
  data() {
    return {
      data: [],
      layout: {
        title: "Desmatamento Anual (km2) da Unidade De Conservação",
      },

    };
  },
  async mounted() {
    const response = await this.$axios.$get(
      `/getDesmatamentoData?uc=${this.uc}`
    );
    this.data.push(response["Line Chart"]);
    this.data.push(response["Bar Chart"])
  },
};
</script>

<style>

</style>