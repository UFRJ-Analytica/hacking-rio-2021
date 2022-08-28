<template>
    <div>
        <Plotly :data="data" :layout="layout" :display-mode-bar="false"></Plotly>
    </div>
</template>

<script>
export default {
  data() {
    return {
        data: [],
        layout: {
            mapbox: {
                style: 'carto-positron',
                center: {
                    lon: -50, 
                    lat: -20
                    }, 
                    zoom: 3.5
                },
            width: 1000, 
            height:1000
        },
    };
  },
  
    async mounted() {
    const response = await this.$axios.$get("/generateRandomData");
    console.log(response)
    console.log(this)
    this.data.push(response)
    },
};
</script>

<style>
</style>