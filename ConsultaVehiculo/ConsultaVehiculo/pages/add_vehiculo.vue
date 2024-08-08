<template>
  <v-container>
    <v-row>
      <v-col>
        <h1 class="text-center mb-5">Agregar nuevo Vehículo</h1>
        <v-form @submit.prevent="submitForm">
          <!-- VIN -->
          <v-text-field
            v-model="form.vin"
            label="VIN"
            outlined
            required
          ></v-text-field>

          <!-- Motor -->
          <v-text-field
            v-model="form.motor"
            label="Motor"
            outlined
            required
          ></v-text-field>

          <!-- Cilindrada -->
          <v-text-field
            v-model="form.cilindrada"
            label="Cilindrada"
            outlined
            required
          ></v-text-field>

          <!-- Año -->
          <v-text-field
            v-model="form.ano"
            label="Año"
            outlined
            required
          ></v-text-field>

          <!-- Marca -->
          <v-text-field
            v-model="form.marca"
            label="Marca"
            outlined
            required
          ></v-text-field>

          <!-- Modelo -->
          <v-text-field
            v-model="form.modelo"
            label="Modelo"
            outlined
            required
          ></v-text-field>

          <!-- Versión -->
          <v-text-field
            v-model="form.version"
            label="Versión"
            outlined
            required
          ></v-text-field>

          <!-- Dueño -->
          <v-text-field
            v-model="form.dueno"
            label="Dueño"
            outlined
            required
          ></v-text-field>

          <!-- Placas -->
          <div class="mb-3">
            <label class="pl-2">Placas:</label>
            <div v-for="(placa, index) in form.placas" :key="index" class="d-flex align-center mb-2">
              <v-text-field
                v-model="placa.patente"
                :label="'Placa ' + (index + 1)"
                outlined
                clearable
                class="mr-2"
              ></v-text-field>
              <v-btn icon @click="removePlaca(index)" v-if="form.placas.length > 1">
                <v-icon>mdi-delete</v-icon>
              </v-btn>
            </div>
            <v-btn text @click="addPlaca" class="pa-2">
              Agregar otra Placa
            </v-btn>
          </div>

          <!-- Submit Button -->
          <v-btn type="submit" color="primary" class="pa-3 mt-3">
            Agregar Vehículo
          </v-btn>
        </v-form>

        <!-- Error and Success Messages -->
        <v-alert v-if="error" type="error" class="mt-4">
          {{ error }}
        </v-alert>
        <v-alert v-if="success" type="success" class="mt-4">
          ¡Vehículo añadido exitosamente!
          <v-btn text @click="resetForm" class="ml-3">Agregar otro</v-btn>
        </v-alert>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from 'vue';
import { useFetch } from '#app';

const form = ref({
  vin: '',
  motor: '',
  cilindrada: '',
  ano: '',
  marca: '',
  modelo: '',
  version: '',
  dueno: '',
  placas: [{ patente: '' }],
});

const error = ref(null);
const success = ref(false);

const submitForm = async () => {
  error.value = null;
  success.value = false;

  try {
    const { data, error: fetchError } = await useFetch('http://127.0.0.1:8000/vehiculos/', {
      method: 'POST',
      body: JSON.stringify(form.value),
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (fetchError.value) {
      console.error('Fetch Error:', fetchError.value);
      throw new Error(fetchError.value.message);
    }

    if (data.value) {
      console.log('Response Data:', data.value);
      success.value = true;
      resetForm();
    }
  } catch (err) {
    console.error('Fetch error:', err);
    error.value = `Error: ${err.message || 'Ocurrió un error inesperado.'}`;
  }
};

const addPlaca = () => {
  form.value.placas.push({ patente: '' });
};

const removePlaca = (index) => {
  form.value.placas.splice(index, 1);
};

const resetForm = () => {
  form.value = {
    vin: '',
    motor: '',
    cilindrada: '',
    ano: '',
    marca: '',
    modelo: '',
    version: '',
    dueno: '',
    placas: [{ patente: '' }],
  };
};
</script>

<style scoped>
.error {
  color: red;
}
</style>
