<template>
  <v-app>
    <v-main>
      <v-toolbar color="#9ACD32">
        <a href="http://www.vale.com/brasil/pt/Paginas/default.aspx">
          <!-- <img
                    src="/logo_horizontal_invertido.png"
                    height="40px"
                    alt="UFRJ Analytica"
                    /> -->
          <img src="/logo-vale-768.png" height="100px" alt="UFRJ Analytica" />
        </a>
        <v-spacer></v-spacer>

        <v-toolbar-title style="color: #696969; font-weight: bold">
        Vale a Pena Conservar
        </v-toolbar-title>


      </v-toolbar>
      <v-container style="padding-top: 30px">
        <Nuxt />
      </v-container>
    </v-main>
    <v-footer color="#9ACD32" padless>
      <v-col class="text-center" style="color: #696969" cols="12">
        <strong>
          <a href="https://ufrjanalytica.ml/">
            <!-- <img
                    src="/logo_horizontal_invertido.png"
                    height="40px"
                    alt="UFRJ Analytica"
                    /> -->
            <img src="/branco_com_brasao.png" height="50px" alt="UFRJ Analytica" />
          </a>
        </strong>
      </v-col>
    </v-footer>
  </v-app>
</template>

<style>
a {
  color: #696969;
}
</style>