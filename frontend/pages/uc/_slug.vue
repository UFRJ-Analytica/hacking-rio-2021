<template>
  <div>
    <h1>{{ this.slug }}</h1>
    <br>
    <notas :uc="this.slug"></notas>
  <plotly-histogram :uc="this.slug"></plotly-histogram>
  <desmatamento-plot :uc="this.slug" ></desmatamento-plot>
  </div>
</template>

<script>
export default {
  async asyncData({ params }) {
    const slug = params.slug; // When calling /abc the slug will be "abc"
    return { slug };
  },
};
</script>