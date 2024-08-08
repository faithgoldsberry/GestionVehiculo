<template>
  <v-container>
    <v-row>
      <v-col>
        <v-btn to="/search" color="primary" class="ma-2">
          Buscar Vehículo
        </v-btn>
        <v-btn to="/add_vehiculo" color="primary" class="ma-2">
          Agregar Vehículo
        </v-btn>
      </v-col>
    </v-row>

    <v-row>
      <v-col>
        <h1 class="text-center">Lista de Vehículos</h1>
        <v-list>
          <v-list-item
            v-for="vehiculo in vehiculos"
            :key="vehiculo.vin"
          >
            <v-card class="mb-3">
              <v-card-title>
                {{ vehiculo.marca }} {{ vehiculo.modelo }} ({{ vehiculo.ano }})
              </v-card-title>
              <v-card-subtitle>
                VIN: {{ vehiculo.vin }}
              </v-card-subtitle>
              <v-card-text>
                <v-list dense>
                  <v-list-item>
                    <v-list-item-content>
                      <v-list-item-title>Motor: {{ vehiculo.motor }}</v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                  <v-list-item>
                    <v-list-item-content>
                      <v-list-item-title>Cilindrada: {{ vehiculo.cilindrada }}</v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                  <v-list-item>
                    <v-list-item-content>
                      <v-list-item-title>Versión: {{ vehiculo.version }}</v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                  <v-list-item>
                    <v-list-item-content>
                      <v-list-item-title>Año: {{ vehiculo.ano }}</v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                  <v-list-item>
                    <v-list-item-content>
                      <v-list-item-title>Marca: {{ vehiculo.marca }}</v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                  <v-list-item>
                    <v-list-item-content>
                      <v-list-item-title>Modelo: {{ vehiculo.modelo }}</v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                  <v-list-item>
                    <v-list-item-content>
                      <v-list-item-title>Dueño: {{ vehiculo.dueno }}</v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list>
                <h3>Placas:</h3>
                <v-list dense>
                  <v-list-item
                    v-for="placa in vehiculo.placas"
                    :key="placa.patente"
                  >
                    {{ placa.patente }}
                  </v-list-item>
                </v-list>
              </v-card-text>
            </v-card>
          </v-list-item>
        </v-list>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'

const { data: vehiculos, error } = useFetch('http://127.0.0.1:8000/vehiculos/')

if (error.value) {
  console.error('Error fetching vehiculos:', error.value)
}
</script>
