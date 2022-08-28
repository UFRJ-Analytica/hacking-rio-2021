

<template>
  <div>
    <v-card color="#385F73" dark>
      <v-card-title class="text-h5"> Nota de Efetividade </v-card-title>

      <v-card-actions>
        <v-btn class="note" text>{{ data["calculo_efetividade_mean"] }}</v-btn>
      </v-card-actions>
    </v-card>

    <br>

    <v-card color="#385F73" dark>
      <v-card-title class="text-h5"> Nota de Apoio </v-card-title>

      <v-card-actions>
        <v-btn class="note" text>{{ data["nota_apoio_mean"] }}</v-btn>
      </v-card-actions>
    </v-card>
    
    <br>

    <v-card color="#385F73" dark>
      <v-card-title class="text-h5"> Nota de Capacidade </v-card-title>

      <v-card-actions>
        <v-btn class="note" text>{{ data["nota_capacidade_mean"] }}</v-btn>
      </v-card-actions>
    </v-card>
    
    <br>

    <v-card color="#385F73" dark>
      <v-card-title class="text-h5"> Nota de Equipamento </v-card-title>

      <v-card-actions>
        <v-btn class="note" text>{{ data["nota_equipamento_mean"] }}</v-btn>
      </v-card-actions>
    </v-card>   
    
    <br>

    <v-card color="#385F73" dark>
      <v-card-title class="text-h5"> Nota Pessoal </v-card-title>

      <v-card-actions>
        <v-btn class="note" text>{{ data["nota_pessoal_mean"] }}</v-btn>
      </v-card-actions>
    </v-card>   
    
    <br>

    <v-card color="#385F73" dark>
      <v-card-title class="text-h5"> Nota Recurso </v-card-title>

      <v-card-actions>
        <v-btn class="note" text>{{ data["nota_recurso_mean"] }}</v-btn>
      </v-card-actions>
    </v-card>    
    
    <br>

  </div>
</template>

<script>
export default {
  props: ["uc"],
  data() {
    return {
      data: {},
    };
  },
  async mounted() {
    const response = await this.$axios.$get(
      `/management_metrics?uc=${this.uc}`
    );
    this.data = response;
  },
};
</script>

<style>
.v-btn.v-size--default {
  font-size: 1.3rem;
}
</style>