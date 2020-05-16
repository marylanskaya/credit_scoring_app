<template>
  <div>
    <h1 align="center">Основная Информация</h1>
    <b-card bg-variant="light" class="mx-auto mt-3" style="width: 90%">
      <b-form @submit='addUser' @reset='clearInfo'>
        <b-form-group
          label-cols-lg="3"
          label="Паспортные данные"
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mx-auto m-0"
          style="width: 100%"
        >
          <b-container class="bv-example-row">
            <b-row class="text-right mt-3">
              <b-col sm="3" align-self="end">
                <label>Тип документа</label>
              </b-col>
              <b-col>
                <b-form-select v-model="document.type">
                  <option :value="null" disabled>Выберите тип документа</option>
                  <option value="passport_rf">Паспорт гражданина РФ</option>
                  <option value="passport_inter">Загранпаспорт иностранного гражданина</option>
                  <option value="another_doc">Иной документ</option>
                </b-form-select>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col sm="3" align-self="end">
                <label>Кем выдан</label>
              </b-col>
              <b-col>
                <b-form-input
                  v-model="document.issue_unit"></b-form-input>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col cols='3' align-self="end">
                <label>Серия</label>
              </b-col>
              <b-col cols='4'>
                <b-form-input
                  v-model="document.series"
                  placeholder="Серия документа"
                  style="width: 90%">
                  </b-form-input>
              </b-col>
              <b-col cols='0' align-self="end">
                <label>Номер</label>
              </b-col>
              <b-col>
                <b-form-input
                  v-model="document.number"
                  placeholder="Номер документа"></b-form-input>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col cols='3' align-self="end">
                <label>Когда выдан</label>
              </b-col>
              <b-col cols='4'>
                <b-form-input
                  v-model="document.issue_date"
                  style="width: 90%"
                  type='date'>
                  </b-form-input>
              </b-col>
              <b-col cols='0' align-self="end">
                <label>Код подразделения</label>
              </b-col>
              <b-col>
                <b-form-input v-model="document.unit_code"></b-form-input>
              </b-col>
            </b-row>
            <b-row>
              <b-button
              type="button"
              variant="primary"
              class="mx-auto mt-3"
              style="width: 30%"
              @click.prevent="findUser"
                >Найти клиента</b-button>
            </b-row>
            <br>
            <b-row class="text-right mt-3">
              <b-col sm="3" align-self="end">
                <label>Фамилия</label>
              </b-col>
              <b-col>
                <b-form-input
                  v-model="user.surname"
                  placeholder="Иванов"></b-form-input>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col sm="3" align-self="end">
                <label>Имя</label>
              </b-col>
              <b-col>
                <b-form-input
                  v-model="user.name"
                  placeholder="Иван"></b-form-input>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col sm="3" align-self="end">
                <label>Отчество</label>
              </b-col>
              <b-col>
                <b-form-input
                  v-model="user.patronymic"
                  placeholder="Иванович"></b-form-input>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col sm="3" align-self="end">
                <label>Дата рождения</label>
              </b-col>
              <b-col>
                <b-form-input
                  v-model="user.birthdate"
                  type="date"></b-form-input>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col sm='3' align-self="end">
                <label>Пол</label>
              </b-col>
              <b-col cols='5'>
                <b-form-radio-group v-model="user.gender">
                  <b-form-radio value="male">Мужской</b-form-radio>
                  <b-form-radio value="female">Женский</b-form-radio>
                </b-form-radio-group>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col sm="3" align-self="end">
                <label>Гражданство</label>
              </b-col>
              <b-col>
                <b-form-input v-model="user.citizenship"></b-form-input>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col sm="3" align-self="end">
                <label>Адрес регистрации</label>
              </b-col>
              <b-col>
                <b-form-input v-model="user.address"></b-form-input>
              </b-col>
            </b-row>
            <b-row align-h="around" align-v="center" class="mt-3">
              <b-col>
                <b-button type='reset' variant="danger" style="width: 100%"
                >Очистить данные</b-button>
              </b-col>
              <b-col>
                <b-button type='submit' variant="success" style="width: 100%"
                >Перейти к заполнению анкеты</b-button>
              </b-col>
            </b-row>
          </b-container>
        </b-form-group>
      </b-form>
    </b-card>
  </div>
</template>

<script>
import axios from 'axios';
import crypto from 'crypto';

export default {
  name: 'Login',
  data() {
    return {
      document: {
        type: 'passport_inter',
        series: '4821',
        number: '21482148',
        issue_unit: 'МВД РК',
        issue_date: '2014-01-22',
        unit_code: '1234',
      },
      user: {
        surname: 'Туркин',
        name: 'Никита',
        patronymic: 'Юрьевич',
        birthdate: '1996-01-22',
        gender: 'male',
        citizenship: 'Казахстан',
        address: 'г.Москва, пр-кт 60-летия Октября, д.11, кв.1616',
      },
    };
  },
  methods: {
    authUser(payload) {
      const path = 'http://localhost:5000/login/auth';
      axios.post(path, payload)
        .then((res) => {
          // eslint-disable-next-line
          console.log(res);
          // eslint-disable-next-line
          console.log(res.data.user_exists);
          if (res.data.user_exists) {
            this.document.type = res.data.data.document.type;
            this.document.series = res.data.data.document.series;
            this.document.number = res.data.data.document.number;
            this.document.issue_unit = res.data.data.document.issue_unit;
            this.document.issue_date = res.data.data.document.issue_date;
            this.document.unit_code = res.data.data.document.unit_code;
            this.user.surname = res.data.data.user.surname;
            this.user.name = res.data.data.user.name;
            this.user.patronymic = res.data.data.user.patronymic;
            this.user.birthdate = res.data.data.user.birthdate;
            this.user.gender = res.data.data.user.gender;
            this.user.citizenship = res.data.data.user.citizenship;
            this.user.address = res.data.data.user.address;
          } else {
          // eslint-disable-next-line
            alert('Данный пользователь не найден!');
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    hashInfo() {
      const secret = 'my-secret';
      const doc = this.document.series + this.document.number;
      const hash = crypto.createHmac('sha256', secret)
        .update(doc)
        .digest('hex');
      return hash;
    },
    findUser(evt) {
      evt.preventDefault();
      const hash = this.hashInfo();
      const payload = {
        user_hash: hash,
        document: {
          type: this.document.type,
          series: this.document.series,
          number: this.document.number,
        },
      };
      this.authUser(payload);
    },
    initForm() {
      this.document.type = '';
      this.document.series = '';
      this.document.number = '';
      this.document.issue_unit = '';
      this.document.issue_date = '';
      this.document.unit_code = '';
      this.user.surname = '';
      this.user.name = '';
      this.user.patronymic = '';
      this.user.birthdate = '';
      this.user.gender = '';
      this.user.citizenship = '';
      this.user.address = '';
    },
    clearInfo(evt) {
      evt.preventDefault();
      this.initForm();
    },
    registerUser(payload) {
      const path = 'http://localhost:5000/login/register';
      axios.post(path, payload)
        .then(() => {
          // eslint-disable-next-line
          console.log(payload);
          const hash = payload.user_hash;
          // eslint-disable-next-line
          console.log(hash);
          this.$router.replace({ name: 'Info', params: { hash } });
          this.$router.push('info');
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    addUser(evt) {
      evt.preventDefault();
      const hash = this.hashInfo();
      const payload = {
        user_hash: hash,
        document: {
          type: this.document.type,
          series: this.document.series,
          number: this.document.number,
          issue_date: this.document.issue_date,
          unit_code: this.document.unit_code,
          issue_unit: this.document.issue_unit,
        },
        user: {
          surname: this.user.surname,
          name: this.user.name,
          patronymic: this.user.patronymic,
          birthdate: this.user.birthdate,
          gender: this.user.gender,
          citizenship: this.user.citizenship,
          address: this.user.address,
        },
      };
      this.registerUser(payload);
    },
  },
  created() {
  },
};
</script>
