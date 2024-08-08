<template>
  <v-container>
    <v-row>
      <v-col>
        <v-form @submit.prevent="search" class="mb-4">
          <v-text-field
            v-model="searchTerm"
            label="Buscar con VIN o Placa"
            outlined
            clearable
          />
          <v-btn type="submit" color="primary" class="ma-2">
            Buscar
          </v-btn>
        </v-form>

        <v-alert v-if="error" type="error" class="mb-4">
          {{ error }}
        </v-alert>

        <div v-if="vehicles && vehicles.length">
          <h2 class="text-center">Resultados</h2>
          <v-list>
            <v-list-item
              v-for="vehicle in vehicles"
              :key="vehicle.vin"
            >
              <v-card class="mb-3">
                <v-card-title>
                  {{ vehicle.marca }} {{ vehicle.modelo }} ({{ vehicle.ano }})
                </v-card-title>
                <v-card-subtitle>
                  VIN: {{ vehicle.vin }}
                </v-card-subtitle>
                <v-card-text>
                  <v-list dense>
                    <v-list-item>
                      <v-list-item-content>
                        <v-list-item-title>Motor: {{ vehicle.motor }}</v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                    <v-list-item>
                      <v-list-item-content>
                        <v-list-item-title>Cilindrada: {{ vehicle.cilindrada }}</v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                    <v-list-item>
                      <v-list-item-content>
                        <v-list-item-title>Versión: {{ vehicle.version }}</v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                    <v-list-item>
                      <v-list-item-content>
                        <v-list-item-title>Año: {{ vehicle.ano }}</v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                    <v-list-item>
                      <v-list-item-content>
                        <v-list-item-title>Marca: {{ vehicle.marca }}</v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                    <v-list-item>
                      <v-list-item-content>
                        <v-list-item-title>Modelo: {{ vehicle.modelo }}</v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                    <v-list-item>
                      <v-list-item-content>
                        <v-list-item-title>Dueño: {{ vehicle.dueno }}</v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list>
                  <h3>Placas:</h3>
                  <v-list dense>
                    <v-list-item
                      v-for="placa in vehicle.placas"
                      :key="placa.patente"
                    >
                      {{ placa.patente }}
                    </v-list-item>
                  </v-list>
                </v-card-text>
              </v-card>
            </v-list-item>
          </v-list>
        </div>

        <v-alert v-else-if="vehicles && !vehicles.length" type="info">
          No se encuentra el vehículo.
        </v-alert>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from 'vue';
import { useFetch } from '#app';

const searchTerm = ref('');
const vehicles = ref(null);
const error = ref(null);

const search = async () => {
  error.value = null;
  vehicles.value = null; // Reset vehicles for successful search handling

  try {
    const { data, error: fetchError } = await useFetch(`http://127.0.0.1:8000/vehiculos/?search=${searchTerm.value}`);

    if (fetchError.value) {
      throw new Error(fetchError.value.message);
    }

    vehicles.value = data.value;
  } catch (err) {
    console.error('Fetch error:', err); // Log the error to the browser console
    error.value = `Error: ${err.message}`;
  }
};
</script>

<style scoped>
.error {
  color: red;
}
</style>
