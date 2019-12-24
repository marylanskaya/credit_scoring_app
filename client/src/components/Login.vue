<template>
  <div>
    <b-card bg-variant="light" class="mx-auto" style="width: 90%;">
      <b-form @submit="onSubmit">
        <b-form-group
          label-cols-lg="3"
          label="Паспортные данные"
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mx-auto m-0"
          style="width: 80%"
        >
          <b-form-group
            label-cols-sm=""
            label="Тип документа"
            label-align-sm="right"
            label-for="nested-document"
            class="m-0"
          >
            <b-form-select v-model="document.type" class="m-0">
              <option :value="null" disabled>Выберите тип документа</option>
              <option value="pass_rf">Паспорт гражданина РФ</option>
              <option value="pass_inter" disabled>
                Загран паспорт иностранного гражданина (disabled)</option>
              <optgroup label="Иные документы">
                <option :value="{ C: '3PO' }">Водительское удостоверение</option>
                <option :value="{ R: '2D2' }">Иной документ</option>
              </optgroup>
            </b-form-select>
          </b-form-group>
          <b-container class="bv-example-row">
            <b-row>
              <b-col sm="1" align-self="center">
                <label>Серия</label>
              </b-col>
              <b-col>
                <b-form-input
                  v-model="document.series"
                  class="m-3"
                  placeholder="Серия документа"></b-form-input>
              </b-col>
              <b-col sm="1" align-self="center">
                <label>Номер</label>
              </b-col>
              <b-col>
                <b-form-input
                  v-model="document.number"
                  class="m-3"
                  placeholder="Номер документа"></b-form-input>
              </b-col>
            </b-row>
            <b-row>
              <b-button type="submit" variant="primary" class="mx-auto" style="width: 30%"
                >Submit</b-button>
            </b-row>
          </b-container>
        </b-form-group>
      </b-form>
    </b-card>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Login',
  data() {
    return {
      document: {
        type: null,
        series: '',
        number: '',
      },
    };
  },
  methods: {
    addDocument(payload) {
      const path = 'http://localhost:5000/login/getdoc';
      axios.post(path, payload)
        .then(() => {
          // eslint-disable-next-line
          console.log('Document added!');
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    onSubmit(evt) {
      evt.preventDefault();
      // eslint-disable-next-line
      console.log('Entered453454534!');
      const payload = {
        document: {
          type: this.document.type,
          series: this.document.series,
          number: this.document.number,
        },
      };
      // eslint-disable-next-line
      console.log('Entered!');
      this.addDocument(payload);
    },
  },
  created() {
  },
};
</script>

<style scoped>
mb-3 {
  margin: auto;
  width: 50%
}
</style>
