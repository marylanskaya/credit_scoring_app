<template>
  <div>
    <h1 align="center">Клиентские данные</h1>
    <b-card bg-variant="light" class="mx-auto mt-3" style="width: 90%">
      <b-form @submit="onSubmit">
        <b-form-group
          label-cols-lg="3"
          label="Общая информация о клиенте"
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mx-auto m-0"
          style="width: 100%"
        >
          <b-container class="bv-example-row">
            <b-row class="text-right mt-3">
              <b-col sm="3" align-self="center">
                <label>Семейное положение</label>
              </b-col>
              <b-col align-self="center">
                <b-form-select v-model="info.name_family_status">
                  <option :value="null" disabled>Выберите семейное положение</option>
                  <option value="Single / not married">Холост / не замужем</option>
                  <option value="Married">Женат / Замужем</option>
                  <option value="Civil marriage">Гражданский брак</option>
                  <option value="Widow">Вдовец / Вдова</option>
                  <option value="Separated">В разводе</option>
                  <option value="Unknown">Неизвестно</option>
                </b-form-select>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col cols='3' align-self="end">
                <label>Количество детей</label>
              </b-col>
              <b-col cols='4'>
                <b-form-input
                  v-model="info.cnt_children"
                  style="width: 90%">
                  </b-form-input>
              </b-col>
              <b-col cols='0' align-self="end">
                <label>Количество членов семьи</label>
              </b-col>
              <b-col>
                <b-form-input
                  v-model="info.cnt_fam_members"></b-form-input>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col cols='3'  align-self="center">
                <b-form-checkbox
                  v-model="info.flag_own_car"
                  style="width: 100%">Есть машина</b-form-checkbox>
              </b-col>
              <b-col cols='4' align-self="end">
                <label>Возраст машины</label>
              </b-col>
              <b-col>
                <b-form-input
                  v-model="info.own_car_age"
                  :disabled="info.flag_own_car == false"
                  style="width: 100%"></b-form-input>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col cols='3.5' align-self="top">
                <b-form-checkbox
                  v-model="info.flag_own_realty" align='left'
                  style="width: 100%">Есть недвижимость</b-form-checkbox>
              </b-col>
              <b-col cols='4' align-self="end">
                <label>Тип дома проживания</label>
              </b-col>
              <b-col align-self="center">
                <b-form-select
                  v-model="info.name_housing_type"
                  style="width: 100%">
                  <option :value="null" disabled>Выберите семейное положение</option>
                  <option value="House / apartment">Дом / квартира</option>
                  <option value="Rented apartment">Съемная квартира</option>
                  <option value="With parents">С родителями</option>
                  <option value="Municipal apartment">Муниципальная квартира</option>
                  <option value="Office apartment">Офисное помещение</option>
                  <option value="Co-op apartment">Кооперативная квартира</option>
                </b-form-select>
              </b-col>
            </b-row>
          </b-container>
        </b-form-group>
        <br>
        <b-form-group
          label-cols-lg="3"
          label="Адрес клиента"
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mx-auto m-0"
          style="width: 100%"
        >
          <b-container class="bv-example-row">
            <b-row class="text-right mt-3">
              <b-col sm="3" align-self="center">
                <label>Область фактического места проживания</label>
              </b-col>
              <b-col align-self="center">
                <b-form-select
                  v-model="info.obl_fact"
                  :options="obl_options">
                </b-form-select>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col sm="3" align-self="end">
                <label>Город фактического места проживания</label>
              </b-col>
              <b-col align-self="center">
                <b-form-select
                  v-model="info.city_fact"
                  :options="city_options">
                </b-form-select>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col sm="2" align-self="center">
                <label>Область места регистрации</label>
              </b-col>
              <b-col sm="4" align-self="center">
                <b-form-checkbox
                  v-model="info.obl_reg_check" align='left'
                  style="width: 100%">Совпадает с местом проживания</b-form-checkbox>
              </b-col>
              <b-col sm="2" align-self="center">
                <label>Город места регистрации</label>
              </b-col>
              <b-col sm="4" align-self="center">
                <b-form-checkbox
                  v-model="info.city_reg_check" align='left'
                  style="width: 100%">Совпадает с местом проживания</b-form-checkbox>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col sm="2" align-self="end">
              </b-col>
              <b-col sm="4" align-self="end">
                <b-form-select
                  :disabled="info.obl_reg_check == true"
                  v-model="info.obl_reg"
                  :options="obl_options">
                </b-form-select>
              </b-col>
              <b-col sm="2" align-self="end">
              </b-col>
              <b-col sm="4" align-self="end">
                <b-form-select
                  :disabled="info.city_reg_check == true"
                  v-model="info.city_reg"
                  :options="city_options">
                </b-form-select>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col sm="2" align-self="center">
                <label>Область места работы</label>
              </b-col>
              <b-col sm="4" align-self="center">
                <b-row class="text-right mt-3">
                  <b-form-checkbox
                    v-model="info.obl_work_fact_check">
                    Совпадает с местом проживания</b-form-checkbox>
                </b-row>
                <b-row class="text-right mt-3">
                  <b-form-checkbox
                  v-model="info.obl_work_reg_check">
                    Совпадает с местом регистрации</b-form-checkbox>
                </b-row>
              </b-col>
              <b-col sm="2" align-self="center">
                <label>Город места работы</label>
              </b-col>
              <b-col sm="4" align-self="center">
                <b-row class="text-right mt-3">
                  <b-form-checkbox
                  v-model="info.city_work_fact_check">
                    Совпадает с местом проживания</b-form-checkbox>
                </b-row>
                <b-row class="text-right mt-3">
                  <b-form-checkbox
                  v-model="info.city_work_reg_check">
                    Совпадает с местом регистрации</b-form-checkbox>
              </b-row>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col sm="2" align-self="end">
              </b-col>
              <b-col sm="4" align-self="end">
                <b-form-select
                  :disabled="(info.obl_work_fact_check || info.obl_work_reg_check)"
                  v-model="info.obl_work"
                  :options="obl_options">
                </b-form-select>
              </b-col>
              <b-col sm="2" align-self="end">
              </b-col>
              <b-col sm="4" align-self="end">
                <b-form-select
                  :disabled="(info.city_work_fact_check || info.city_work_reg_check)"
                  v-model="info.city_work"
                  :options="city_options">
                </b-form-select>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col cols='3' align-self="end">
                <label>Мобильный телефон</label>
              </b-col>
              <b-col>
                <b-form-input
                  v-model="info.mobile"
                  style="width: 100%"></b-form-input>
              </b-col>
              <b-col cols='3'  align-self="center">
                <b-form-checkbox
                v-model="info.mobile_check"
                style="width: 100%">Подтвержден</b-form-checkbox>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col cols='3' align-self="end">
                <label>Рабочий телефон</label>
              </b-col>
              <b-col>
                <b-form-input
                  v-model="info.work_phone"
                  style="width: 100%"></b-form-input>
              </b-col>
              <b-col cols='3' align-self="end">
                <label>Домашний телефон</label>
              </b-col>
              <b-col>
                <b-form-input
                  v-model="info.home_phone"
                  style="width: 100%"></b-form-input>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col cols='3' align-self="end">
                <label>Email</label>
              </b-col>
              <b-col>
                <b-form-input
                  v-model="info.email"
                  style="width: 100%"></b-form-input>
              </b-col>
            </b-row>
          </b-container>
        </b-form-group>
        <br>
        <b-form-group
          label-cols-lg="3"
          label="Сведения о занятости"
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mx-auto m-0"
          style="width: 100%"
        >
          <b-container class="bv-example-row">
            <b-row class="text-right mt-3">
              <b-col sm="3" align-self="center">
                <label>Трудовой статус</label>
              </b-col>
              <b-col align-self="center">
                <b-form-select v-model="info.work_status">
                  <option :value="null" disabled>Выберите трудовой статус</option>
                  <option value="Working">Работа по договору</option>
                  <option value="Commercial associate">Коммерческий партнер</option>
                  <option value="State servant">Государственный служащий</option>
                  <option value="Businessman">Бизнесмен</option>
                  <option value="Maternity leave">Декретный отпуск</option>
                  <option value="Student">Студент</option>
                  <option value="Pensioner">Пенсионер</option>
                  <option value="Unemployed">Безработный</option>
                </b-form-select>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col cols='3' align-self="end">
                <label>Стаж на текущем месте работы (мес.)</label>
              </b-col>
              <b-col>
                <b-form-input
                  :disabled="info.work_status == 'unemployed'"
                  v-model="info.work_exp"
                  style="width: 100%"></b-form-input>
              </b-col>
            </b-row>
            <!-- <b-row class="text-right mt-3">
              <b-col sm="3" align-self="center">
                <label>Отрасль компании</label>
              </b-col>
              <b-col align-self="center">
                <b-form-select
                  v-model="info.name_family_status">
                  <option :value="null" disabled>Выберите семейное положение</option>
                  <option value="single">Холост / не замужем</option>
                  <option value="married">Женат / Замужем</option>
                  <option value="civil_marriage">Гражданский брак</option>
                  <option value="Widow">Вдовец / Вдова</option>
                  <option value="separated">В разводе</option>
                  <option value="unknown">Неизвестно</option>
                </b-form-select>
              </b-col>
            </b-row> -->
            <b-row class="text-right mt-3">
              <b-col sm="3" align-self="center">
                <label>Тип организации</label>
              </b-col>
              <b-col align-self="center">
                <b-form-select
                  :disabled="info.work_status == 'unemployed'"
                  v-model="info.organization_type"
                  :options='organization_type_options'>
                </b-form-select>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col cols='3' align-self="end">
                <label>Профессия</label>
              </b-col>
              <b-col>
                <b-form-select
                  :disabled="info.work_status == 'unemployed'"
                  v-model="info.position_cat"
                  :options='occupation_type_options'>
                </b-form-select>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col cols='3' align-self="end">
                <label>Доход по основному месту работы</label>
              </b-col>
              <b-col>
                <b-form-input
                  :disabled="info.work_status == 'unemployed'"
                  v-model="info.main_income"
                  style="width: 100%"></b-form-input>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col cols='3' align-self="end">
                <label>Дополнительный Доход</label>
              </b-col>
              <b-col>
                <b-form-input
                  v-model="info.second_income"
                  style="width: 100%"></b-form-input>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col sm="3" align-self="center">
                <label>Уровень образования</label>
              </b-col>
              <b-col align-self="center">
                <b-form-select
                  v-model="info.edu_type"
                  :options="education_type_options"></b-form-select>
              </b-col>
            </b-row>
          </b-container>
        </b-form-group>
        <br>
        <b-form-group
          label-cols-lg="3"
          label="Предоставлено"
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mx-auto m-0"
          style="width: 100%"
        >
          <b-container class="bv-example-row">
            <b-row class="text-right mt-3">
              <b-form-checkbox v-model="info.own_inn">ИНН</b-form-checkbox>
            </b-row>
            <b-row class="text-right mt-3">
              <b-form-checkbox v-model="info.own_ndfl">2-НДФЛ</b-form-checkbox>
            </b-row>
            <b-row class="text-right mt-3">
              <b-form-checkbox v-model="info.own_snils">СНИЛС</b-form-checkbox>
            </b-row>
            <b-row class="text-right mt-3">
              <b-form-checkbox v-model="info.own_forepass">Загранпаспорт</b-form-checkbox>
            </b-row>
            <b-row class="text-right mt-3">
              <b-form-checkbox v-model="info.own_prev_app">
              Есть непогашенные кредиты</b-form-checkbox>
            </b-row>
          </b-container>
        </b-form-group>
        <br>
        <b-form-group
          label-cols-lg="3"
          label="Сведения о кредите"
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mx-auto m-0"
          style="width: 100%"
        >
          <b-container class="bv-example-row">
            <b-row class="text-right mt-3">
              <b-col sm="3" align-self="center">
                <label>Тип кредита</label>
              </b-col>
              <b-col align-self="center">
                <b-form-select v-model="info.cred_type">
                  <option :value="null" disabled>Выберите тип кредита</option>
                  <option value="cred_potreb">Потребительский кредит</option>
                  <option value="cred_nal">Кредит наличными</option>
                  <option value="cred_vozob">Возобновляемый кредит</option>
                </b-form-select>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col sm="3" align-self="center">
                <label>Сумма на товары</label>
              </b-col>
              <b-col align-self="center">
                <b-form-input
                  v-model="info.goods_sum"
                  :disabled="info.cred_type != 'cred_potreb'"
                  style="width: 100%"></b-form-input>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col sm="3" align-self="center">
                <label>Сумма кредита</label>
              </b-col>
              <b-col align-self="center">
                <b-form-input
                  v-model="info.cred_sum"
                  style="width: 100%"></b-form-input>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col sm="3" align-self="center">
                <label>Цель кредита</label>
              </b-col>
              <b-col align-self="center">
                <b-form-select
                  v-model="info.credit_purpose"
                  :options="credit_purpose_options">
                </b-form-select>
              </b-col>
            </b-row>
            <b-row class="text-right mt-3">
              <b-col sm="3" align-self="center">
                <label>Дата подачи заявления на кредит</label>
              </b-col>
              <b-col>
                <b-form-input
                  v-model="info.credit_date"
                  type="date"></b-form-input>
              </b-col>
            </b-row>
            <b-row align-h="around" align-v="center" class="mt-3">
              <b-col>
                <b-button href='/login' variant="danger" style="width: 100%"
                >Вернуться к предыдущей форме</b-button>
              </b-col>
              <b-col>
                <b-button type='submit' variant="success" style="width: 100%"
                >Показать результаты скоринга</b-button>
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

export default {
  name: 'Login',
  props: ['hash'],
  data() {
    return {
      credit_purpose_options: [
        { value: null, text: 'Выберите цель кредитования' },
        { value: 'Repairs', text: 'Ремонт' },
        { value: 'Everyday expenses', text: 'Повседневные расходы' },
        { value: 'Car repairs', text: 'Автомобильный ремонт' },
        { value: 'Building a house or an annex', text: 'Строительство' },
        { value: 'Journey', text: 'Путешествие' },
        { value: 'Purchase of electronic equipment',
          text: 'Приобретение электронного оборудования' },
        { value: 'Medicine', text: 'Медикаменты' },
        { value: 'Payments on other loans', text: 'Платежи по прочим кредитам' },
        { value: 'Urgent needs', text: 'Срочная необходимость' },
        { value: 'Buying a used car', text: 'Покупка подержанного автомобиля' },
        { value: 'Buying a new car', text: 'Покупка нового автомобиля' },
        { value: 'Buying a home', text: 'Покупка дома' },
        { value: 'Buying a holiday home / land', text: 'Покупка дачи' },
        { value: 'Buying a garage', text: 'Покупка гаража' },
        { value: 'Education', text: 'Образование' },
        { value: 'Furniture', text: 'Мебель' },
        { value: 'Business development', text: 'Развитие бизнеса' },
        { value: 'Wedding / gift / holiday', text: 'Свадьба / подарок / праздник' },
        { value: 'Hobby', text: 'Хобби' },
        { value: 'Gasification / water supply', text: 'Газификация / водоснабжение' },
        { value: 'Money for a third person', text: 'Деньги для третьего лица' },
        { value: 'Refusal to name the goal', text: 'Отказ назвать цель' },
        { value: 'Other', text: 'Другое' },
      ],
      education_type_options: [
        { value: null, text: 'Выберите уровень образования' },
        { value: 'Lower secondary', text: 'Образование ниже среднего' },
        { value: 'Secondary / secondary special', text: 'Среднее / специальное образование' },
        { value: 'Incomplete higher', text: 'Неполное высшее образование' },
        { value: 'Higher education', text: 'Высшее образование' },
        { value: 'Academic degree', text: 'Ученая степень' },
      ],
      occupation_type_options: [
        { value: null, text: 'Выберите профессию' },
        { value: 'Realty agents', text: 'Агент по недвижимости' },
        { value: 'Accountants', text: 'Бухгалтеры' },
        { value: 'Drivers', text: 'Водители' },
        { value: 'High skill tech staff', text: 'Высококвалифицированный технический персонал' },
        { value: 'Managers', text: 'Менеджер' },
        { value: 'IT staff', text: 'ИТ-персонал' },
        { value: 'Cleaning staff', text: 'Клининговый персонал' },
        { value: 'Cooking staff', text: 'Кулинарный персонал' },
        { value: 'Private service staff', text: 'Личный обслуживающий персонал' },
        { value: 'Medicine staff', text: 'Медицинский персонал' },
        { value: 'Low-skill Laborers', text: 'Низкоквалифицированные рабочие' },
        { value: 'Core staff', text: 'Основной персонал' },
        { value: 'Waiters/barmen staff', text: 'Официанты / бармены персонал' },
        { value: 'HR staff', text: 'Персонал отдела кадров' },
        { value: 'Laborers', text: 'Рабочие' },
        { value: 'Secretaries', text: 'Секретари' },
        { value: 'Security staff', text: 'Сотрудник службы безопасности' },
        { value: 'Sales staff', text: 'Торговый персонал' },
      ],
      organization_type_options: [
        { value: null, text: 'Выберите тип организации' },
        { value: 'type 1', text: 'ООО – Общество с ограниченной ответственностью' },
        { value: 'type 2', text: 'АО – Акционерное общество' },
        { value: 'type 3', text: 'ОАО – Открытое акционерное общество' },
        { value: 'type 4', text: 'ЗАО - Закрытое акционерное общество' },
        { value: 'type 5', text: 'ИП – индивидуальный предприниматель' },
        { value: 'type 6', text: 'НКО (НО) – некоммерческая организация' },
      ],
      obl_options: [
        { value: null, text: 'Выберите область', disabled: true },
        { value: 'amur', text: 'Амурская область' },
        { value: 'arkhangelsk', text: 'Архангельская область' },
        { value: 'astrakhan', text: 'Астраханская область' },
        { value: 'belgorod', text: 'Белгородская область' },
        { value: 'bryansk', text: 'Брянская область' },
        { value: 'vladimir', text: 'Владимирская область' },
        { value: 'volgograd', text: 'Волгоградская область' },
        { value: 'vologda', text: 'Вологодская область' },
        { value: 'voronezh', text: 'Воронежская область' },
        { value: 'ivanovskaya', text: 'Ивановская область' },
        { value: 'irkutsk', text: 'Иркутская область' },
        { value: 'kaliningrad', text: 'Калининградская область' },
        { value: 'kaluga', text: 'Калужская область' },
        { value: 'kemerovo', text: 'Кемеровская область' },
        { value: 'kirov', text: 'Кировская область' },
        { value: 'kostroma', text: 'Костромская область' },
        { value: 'kurgan', text: 'Курганская область' },
        { value: 'kursk', text: 'Курская область' },
        { value: 'leningrad', text: 'Ленинградская область' },
        { value: 'lipetsk', text: 'Липецкая область' },
        { value: 'magadan', text: 'Магаданская область' },
        { value: 'moscow', text: 'Московская область' },
        { value: 'murmansk', text: 'Мурманская область' },
        { value: 'nizhniy_novgorod', text: 'Нижегородская область' },
        { value: 'novgorodian', text: 'Новгородская область' },
        { value: 'novosibirsk', text: 'Новосибирская область' },
        { value: 'omsky', text: 'Омская область' },
        { value: 'orenburg', text: 'Оренбургская область' },
        { value: 'orlowski', text: 'Орловская область' },
        { value: 'penza', text: 'Пензенская область' },
        { value: 'pskov', text: 'Псковская область' },
        { value: 'rostov', text: 'Ростовская область' },
        { value: 'ryazan', text: 'Рязанская область' },
        { value: 'samara', text: 'Самарская область' },
        { value: 'saratov', text: 'Саратовская область' },
        { value: 'sakhalin', text: 'Сахалинская область' },
        { value: 'sverdlovsk', text: 'Свердловская область' },
        { value: 'smolensk', text: 'Смоленская область' },
        { value: 'tambov', text: 'Тамбовская область' },
        { value: 'tverskaya', text: 'Тверская область' },
        { value: 'tomsk', text: 'Томская область' },
        { value: 'tula', text: 'Тульская область' },
        { value: 'tumen', text: 'Тюменская область' },
        { value: 'ulyanovsk', text: 'Ульяновская область' },
        { value: 'chelyabinsk', text: 'Челябинская область' },
        { value: 'yaroslavl', text: 'Ярославская область' },
        { value: 'jewish', text: 'Еврейская автономная область' },
      ],
      city_options: [
        { value: null, text: 'Выберите город', disabled: true },
        { value: '1', text: 'Абаза' },
        { value: '2', text: 'Абакан' },
        { value: '3', text: 'Абдулино' },
        { value: '4', text: 'Абинск' },
        { value: '5', text: 'Агидель' },
        { value: '6', text: 'Агрыз' },
        { value: '7', text: 'Адыгейск' },
        { value: '8', text: 'Азнакаево' },
        { value: '9', text: 'Азов' },
        { value: '10', text: 'Ак-Довурак' },
        { value: '11', text: 'Аксай' },
        { value: '12', text: 'Алагир' },
        { value: '13', text: 'Алапаевск' },
        { value: '14', text: 'Алатырь' },
        { value: '15', text: 'Алдан' },
        { value: '16', text: 'Алейск' },
        { value: '17', text: 'Александров' },
        { value: '18', text: 'Александровск' },
        { value: '19', text: 'Александровск-Сахалинский' },
        { value: '20', text: 'Алексеевка' },
        { value: '21', text: 'Алексин' },
        { value: '22', text: 'Алзамай' },
        { value: '23', text: 'Алупка' },
        { value: '24', text: 'Алушта' },
        { value: '25', text: 'Альметьевск' },
        { value: '26', text: 'Амурск' },
        { value: '27', text: 'Анадырь' },
        { value: '28', text: 'Анапа' },
        { value: '29', text: 'Ангарск' },
        { value: '30', text: 'Андреаполь' },
        { value: '31', text: 'Анжеро-Судженск' },
        { value: '32', text: 'Анива' },
        { value: '33', text: 'Апатиты' },
        { value: '34', text: 'Апрелевка' },
        { value: '35', text: 'Апшеронск' },
        { value: '36', text: 'Арамиль' },
        { value: '37', text: 'Аргун' },
        { value: '38', text: 'Ардатов' },
        { value: '39', text: 'Ардон' },
        { value: '40', text: 'Арзамас' },
        { value: '41', text: 'Аркадак' },
        { value: '42', text: 'Армавир' },
        { value: '43', text: 'Армянск' },
        { value: '44', text: 'Армянськ' },
        { value: '45', text: 'Арсеньев' },
        { value: '46', text: 'Арск' },
        { value: '47', text: 'Артем' },
        { value: '48', text: 'Артемовск' },
        { value: '49', text: 'Артемовский' },
        { value: '50', text: 'Архангельск' },
        { value: '51', text: 'Асбест' },
        { value: '52', text: 'Асино' },
        { value: '53', text: 'Астрахань' },
        { value: '54', text: 'Аткарск' },
        { value: '55', text: 'Ахтубинск' },
        { value: '56', text: 'Ахтубинск-7' },
        { value: '57', text: 'Ачинск' },
        { value: '58', text: 'Аша' },
        { value: '59', text: 'Бабаево' },
        { value: '60', text: 'Бабушкин' },
        { value: '61', text: 'Бавлы' },
        { value: '62', text: 'Багратионовск' },
        { value: '63', text: 'Байкальск' },
        { value: '64', text: 'Баймак' },
        { value: '65', text: 'Бакал' },
        { value: '66', text: 'Баксан' },
        { value: '67', text: 'Балабаново' },
        { value: '68', text: 'Балаково' },
        { value: '69', text: 'Балахна' },
        { value: '70', text: 'Балашиха' },
        { value: '71', text: 'Балашов' },
        { value: '72', text: 'Балей' },
        { value: '73', text: 'Балтийск' },
        { value: '74', text: 'Барабинск' },
        { value: '75', text: 'Барнаул' },
        { value: '76', text: 'Барыш' },
        { value: '77', text: 'Батайск' },
        { value: '78', text: 'Бахчисарай' },
        { value: '79', text: 'Бежецк' },
        { value: '80', text: 'Белая Калитва' },
        { value: '81', text: 'Белая Холуница' },
        { value: '82', text: 'Белгород' },
        { value: '83', text: 'Белебей' },
        { value: '84', text: 'Белев' },
        { value: '85', text: 'Белинский' },
        { value: '86', text: 'Белово' },
        { value: '87', text: 'Белогорск' },
        { value: '88', text: 'Белогорск' },
        { value: '89', text: 'Белозерск' },
        { value: '90', text: 'Белокуриха' },
        { value: '91', text: 'Беломорск' },
        { value: '92', text: 'Белорецк' },
        { value: '93', text: 'Белореченск' },
        { value: '94', text: 'Белоусово' },
        { value: '95', text: 'Белоярский' },
        { value: '96', text: 'Белый' },
        { value: '97', text: 'Бердск' },
        { value: '98', text: 'Березники' },
        { value: '99', text: 'Березовский' },
        { value: '100', text: 'Березовский' },
        { value: '101', text: 'Беслан' },
        { value: '102', text: 'Бийск' },
        { value: '103', text: 'Бикин' },
        { value: '104', text: 'Билибино' },
        { value: '105', text: 'Биробиджан' },
        { value: '106', text: 'Бирск' },
        { value: '107', text: 'Бирюсинск' },
        { value: '108', text: 'Бирюч' },
        { value: '109', text: 'Благовещенск' },
        { value: '110', text: 'Благовещенск' },
        { value: '111', text: 'Благодарный' },
        { value: '112', text: 'Бобров' },
        { value: '113', text: 'Богданович' },
        { value: '114', text: 'Богородицк' },
        { value: '115', text: 'Богородск' },
        { value: '116', text: 'Боготол' },
        { value: '117', text: 'Богучар' },
        { value: '118', text: 'Бодайбо' },
        { value: '119', text: 'Бокситогорск' },
        { value: '120', text: 'Болгар' },
        { value: '121', text: 'Бологое' },
        { value: '122', text: 'Болотное' },
        { value: '123', text: 'Болохово' },
        { value: '124', text: 'Болхов' },
        { value: '125', text: 'Большой Камень' },
        { value: '126', text: 'Бор' },
        { value: '127', text: 'Борзя' },
        { value: '128', text: 'Борисоглебск' },
        { value: '129', text: 'Боровичи' },
        { value: '130', text: 'Боровск' },
        { value: '131', text: 'Боровск-1' },
        { value: '132', text: 'Бородино' },
        { value: '133', text: 'Братск' },
        { value: '134', text: 'Бронницы' },
        { value: '135', text: 'Брянск' },
        { value: '136', text: 'Бугульма' },
        { value: '137', text: 'Бугуруслан' },
        { value: '138', text: 'Буденновск' },
        { value: '139', text: 'Бузулук' },
        { value: '140', text: 'Буинск' },
        { value: '141', text: 'Буй' },
        { value: '142', text: 'Буйнакск' },
        { value: '143', text: 'Бутурлиновка' },
        { value: '144', text: 'Валдай' },
        { value: '145', text: 'Валуйки' },
        { value: '146', text: 'Велиж' },
        { value: '147', text: 'Великие Луки' },
        { value: '148', text: 'Великие Луки-1' },
        { value: '149', text: 'Великий Новгород' },
        { value: '150', text: 'Великий Устюг' },
        { value: '151', text: 'Вельск' },
        { value: '152', text: 'Венев' },
        { value: '153', text: 'Верещагино' },
        { value: '154', text: 'Верея' },
        { value: '155', text: 'Верхнеуральск' },
        { value: '156', text: 'Верхний Тагил' },
        { value: '157', text: 'Верхний Уфалей' },
        { value: '158', text: 'Верхняя Пышма' },
        { value: '159', text: 'Верхняя Салда' },
        { value: '160', text: 'Верхняя Тура' },
        { value: '161', text: 'Верхотурье' },
        { value: '162', text: 'Верхоянск' },
        { value: '163', text: 'Весьегонск' },
        { value: '164', text: 'Ветлуга' },
        { value: '165', text: 'Видное' },
        { value: '166', text: 'Вилюйск' },
        { value: '167', text: 'Вилючинск' },
        { value: '168', text: 'Вихоревка' },
        { value: '169', text: 'Вичуга' },
        { value: '170', text: 'Владивосток' },
        { value: '171', text: 'Владикавказ' },
        { value: '172', text: 'Владимир' },
        { value: '173', text: 'Волгоград' },
        { value: '174', text: 'Волгодонск' },
        { value: '175', text: 'Волгореченск' },
        { value: '176', text: 'Волжск' },
        { value: '177', text: 'Волжский' },
        { value: '178', text: 'Вологда' },
        { value: '179', text: 'Володарск' },
        { value: '180', text: 'Волоколамск' },
        { value: '181', text: 'Волосово' },
        { value: '182', text: 'Волхов' },
        { value: '183', text: 'Волчанск' },
        { value: '184', text: 'Вольск' },
        { value: '185', text: 'Вольск-18' },
        { value: '186', text: 'Воркута' },
        { value: '187', text: 'Воронеж' },
        { value: '188', text: 'Воронеж-45' },
        { value: '189', text: 'Ворсма' },
        { value: '190', text: 'Воскресенск' },
        { value: '191', text: 'Воткинск' },
        { value: '192', text: 'Всеволожск' },
        { value: '193', text: 'Вуктыл' },
        { value: '194', text: 'Выборг' },
        { value: '195', text: 'Выкса' },
        { value: '196', text: 'Высоковск' },
        { value: '197', text: 'Высоцк' },
        { value: '198', text: 'Вытегра' },
        { value: '199', text: 'Вышний Волочек' },
        { value: '200', text: 'Вяземский' },
        { value: '201', text: 'Вязники' },
        { value: '202', text: 'Вязьма' },
        { value: '203', text: 'Вятские Поляны' },
        { value: '204', text: 'Гаврилов Посад' },
        { value: '205', text: 'Гаврилов-Ям' },
        { value: '206', text: 'Гагарин' },
        { value: '207', text: 'Гаджиево' },
        { value: '208', text: 'Гай' },
        { value: '209', text: 'Галич' },
        { value: '210', text: 'Гатчина' },
        { value: '211', text: 'Гвардейск' },
        { value: '212', text: 'Гдов' },
        { value: '213', text: 'Геленджик' },
        { value: '214', text: 'Георгиевск' },
        { value: '215', text: 'Глазов' },
        { value: '216', text: 'Голицыно' },
        { value: '217', text: 'Горбатов' },
        { value: '218', text: 'Горно-Алтайск' },
        { value: '219', text: 'Горнозаводск' },
        { value: '220', text: 'Горняк' },
        { value: '221', text: 'Городец' },
        { value: '222', text: 'Городище' },
        { value: '223', text: 'Городовиковск' },
        { value: '224', text: 'Городской округ Черноголовка' },
        { value: '225', text: 'Гороховец' },
        { value: '226', text: 'Горячий Ключ' },
        { value: '227', text: 'Грайворон' },
        { value: '228', text: 'Гремячинск' },
        { value: '229', text: 'Грозный' },
        { value: '230', text: 'Грязи' },
        { value: '231', text: 'Грязовец' },
        { value: '232', text: 'Губаха' },
        { value: '233', text: 'Губкин' },
        { value: '234', text: 'Губкинский' },
        { value: '235', text: 'Гудермес' },
        { value: '236', text: 'Гуково' },
        { value: '237', text: 'Гулькевичи' },
        { value: '238', text: 'Гурьевск' },
        { value: '239', text: 'Гурьевск' },
        { value: '240', text: 'Гусев' },
        { value: '241', text: 'Гусиноозерск' },
        { value: '242', text: 'Гусь-Хрустальный' },
        { value: '243', text: 'Давлеканово' },
        { value: '244', text: 'Дагестанские Огни' },
        { value: '245', text: 'Далматово' },
        { value: '246', text: 'Дальнегорск' },
        { value: '247', text: 'Дальнереченск' },
        { value: '248', text: 'Данилов' },
        { value: '249', text: 'Данков' },
        { value: '250', text: 'Дегтярск' },
        { value: '251', text: 'Дедовск' },
        { value: '252', text: 'Демидов' },
        { value: '253', text: 'Дербент' },
        { value: '254', text: 'Десногорск' },
        { value: '255', text: 'Джанкой' },
        { value: '256', text: 'Джанкой' },
        { value: '257', text: 'Дзержинск' },
        { value: '258', text: 'Дзержинский' },
        { value: '259', text: 'Дивногорск' },
        { value: '260', text: 'Дигора' },
        { value: '261', text: 'Димитровград' },
        { value: '262', text: 'Дмитриев' },
        { value: '263', text: 'Дмитров' },
        { value: '264', text: 'Дмитровск' },
        { value: '265', text: 'Дно' },
        { value: '266', text: 'Добрянка' },
        { value: '267', text: 'Долгопрудный' },
        { value: '268', text: 'Долинск' },
        { value: '269', text: 'Домодедово' },
        { value: '270', text: 'Донецк' },
        { value: '271', text: 'Донской' },
        { value: '272', text: 'Дорогобуж' },
        { value: '273', text: 'Дрезна' },
        { value: '274', text: 'Дубна' },
        { value: '275', text: 'Дубовка' },
        { value: '276', text: 'Дудинка' },
        { value: '277', text: 'Духовщина' },
        { value: '278', text: 'Дюртюли' },
        { value: '279', text: 'Дятьково' },
        { value: '280', text: 'Евпатория' },
        { value: '281', text: 'Егорьевск' },
        { value: '282', text: 'Ейск' },
        { value: '283', text: 'Екатеринбург' },
        { value: '284', text: 'Елабуга' },
        { value: '285', text: 'Елец' },
        { value: '286', text: 'Елизово' },
        { value: '287', text: 'Ельня' },
        { value: '288', text: 'Еманжелинск' },
        { value: '289', text: 'Емва' },
        { value: '290', text: 'Енисейск' },
        { value: '291', text: 'Ермолино' },
        { value: '292', text: 'Ершов' },
        { value: '293', text: 'Ессентуки' },
        { value: '294', text: 'Ефремов' },
        { value: '295', text: 'Железноводск' },
        { value: '296', text: 'Железногорск' },
        { value: '297', text: 'Железногорск' },
        { value: '298', text: 'Железногорск-Илимский' },
        { value: '299', text: 'Железнодорожный' },
        { value: '300', text: 'Жердевка' },
        { value: '301', text: 'Жигулевск' },
        { value: '302', text: 'Жиздра' },
        { value: '303', text: 'Жирновск' },
        { value: '304', text: 'Жуков' },
        { value: '305', text: 'Жуковка' },
        { value: '306', text: 'Жуковский' },
        { value: '307', text: 'Завитинск' },
        { value: '308', text: 'Заводоуковск' },
        { value: '309', text: 'Заволжск' },
        { value: '310', text: 'Заволжье' },
        { value: '311', text: 'Задонск' },
        { value: '312', text: 'Заинск' },
        { value: '313', text: 'Закаменск' },
        { value: '314', text: 'Заозерный' },
        { value: '315', text: 'Заозерск' },
        { value: '316', text: 'Западная Двина' },
        { value: '317', text: 'Заполярный' },
        { value: '318', text: 'Зарайск' },
        { value: '319', text: 'Заречный' },
        { value: '320', text: 'Заречный' },
        { value: '321', text: 'Заринск' },
        { value: '322', text: 'Звенигово' },
        { value: '323', text: 'Звенигород' },
        { value: '324', text: 'Зверево' },
        { value: '325', text: 'Зеленогорск' },
        { value: '326', text: 'Зеленогорск' },
        { value: '327', text: 'Зеленоград' },
        { value: '328', text: 'Зеленоградск' },
        { value: '329', text: 'Зеленодольск' },
        { value: '330', text: 'Зеленокумск' },
        { value: '331', text: 'Зерноград' },
        { value: '332', text: 'Зея' },
        { value: '333', text: 'Зима' },
        { value: '334', text: 'Златоуст' },
        { value: '335', text: 'Злынка' },
        { value: '336', text: 'Змеиногорск' },
        { value: '337', text: 'Знаменск' },
        { value: '338', text: 'Зубцов' },
        { value: '339', text: 'Зуевка' },
        { value: '340', text: 'Ивангород' },
        { value: '341', text: 'Иваново' },
        { value: '342', text: 'Ивантеевка' },
        { value: '343', text: 'Ивдель' },
        { value: '344', text: 'Игарка' },
        { value: '345', text: 'Ижевск' },
        { value: '346', text: 'Избербаш' },
        { value: '347', text: 'Изобильный' },
        { value: '348', text: 'Иланский' },
        { value: '349', text: 'Инза' },
        { value: '350', text: 'Инкерман' },
        { value: '351', text: 'Инсар' },
        { value: '352', text: 'Инта' },
        { value: '353', text: 'Ипатово' },
        { value: '354', text: 'Ирбит' },
        { value: '355', text: 'Иркутск' },
        { value: '356', text: 'Иркутск-45' },
        { value: '357', text: 'Исилькуль' },
        { value: '358', text: 'Искитим' },
        { value: '359', text: 'Истра' },
        { value: '360', text: 'Истра-1' },
        { value: '361', text: 'Ишим' },
        { value: '362', text: 'Ишимбай' },
        { value: '363', text: 'Йошкар-Ола' },
        { value: '364', text: 'Кадников' },
        { value: '365', text: 'Казань' },
        { value: '366', text: 'Калач' },
        { value: '367', text: 'Калачинск' },
        { value: '368', text: 'Калач-на-Дону' },
        { value: '369', text: 'Калининград' },
        { value: '370', text: 'Калининск' },
        { value: '371', text: 'Калтан' },
        { value: '372', text: 'Калуга' },
        { value: '373', text: 'Калязин' },
        { value: '374', text: 'Камбарка' },
        { value: '375', text: 'Каменка' },
        { value: '376', text: 'Каменногорск' },
        { value: '377', text: 'Каменск-Уральский' },
        { value: '378', text: 'Каменск-Шахтинский' },
        { value: '379', text: 'Камень-на-Оби' },
        { value: '380', text: 'Камешково' },
        { value: '381', text: 'Камызяк' },
        { value: '382', text: 'Камышин' },
        { value: '383', text: 'Камышлов' },
        { value: '384', text: 'Канаш' },
        { value: '385', text: 'Кандалакша' },
        { value: '386', text: 'Канск' },
        { value: '387', text: 'Карабаново' },
        { value: '388', text: 'Карабаш' },
        { value: '389', text: 'Карабулак' },
        { value: '390', text: 'Карасук' },
        { value: '391', text: 'Карачаевск' },
        { value: '392', text: 'Карачев' },
        { value: '393', text: 'Каргат' },
        { value: '394', text: 'Каргополь' },
        { value: '395', text: 'Карпинск' },
        { value: '396', text: 'Карталы' },
        { value: '397', text: 'Касимов' },
        { value: '398', text: 'Касли' },
        { value: '399', text: 'Каспийск' },
        { value: '400', text: 'Катав-Ивановск' },
        { value: '401', text: 'Катайск' },
        { value: '402', text: 'Качканар' },
        { value: '403', text: 'Кашин' },
        { value: '404', text: 'Кашира' },
        { value: '405', text: 'Кашира-8' },
        { value: '406', text: 'Кедровый' },
        { value: '407', text: 'Кемерово' },
        { value: '408', text: 'Кемь' },
        { value: '409', text: 'Керчь' },
        { value: '410', text: 'Кизел' },
        { value: '411', text: 'Кизилюрт' },
        { value: '412', text: 'Кизляр' },
        { value: '413', text: 'Кимовск' },
        { value: '414', text: 'Кимры' },
        { value: '415', text: 'Кингисепп' },
        { value: '416', text: 'Кинель' },
        { value: '417', text: 'Кинешма' },
        { value: '418', text: 'Киреевск' },
        { value: '419', text: 'Киренск' },
        { value: '420', text: 'Киржач' },
        { value: '421', text: 'Кириллов' },
        { value: '422', text: 'Кириши' },
        { value: '423', text: 'Киров' },
        { value: '424', text: 'Киров' },
        { value: '425', text: 'Кировград' },
        { value: '426', text: 'Кирово-Чепецк' },
        { value: '427', text: 'Кировск' },
        { value: '428', text: 'Кировск' },
        { value: '429', text: 'Кирс' },
        { value: '430', text: 'Кирсанов' },
        { value: '431', text: 'Киселевск' },
        { value: '432', text: 'Кисловодск' },
        { value: '433', text: 'Климовск' },
        { value: '434', text: 'Клин' },
        { value: '435', text: 'Клинцы' },
        { value: '436', text: 'Княгинино' },
        { value: '437', text: 'Ковдор' },
        { value: '438', text: 'Ковров' },
        { value: '439', text: 'Ковылкино' },
        { value: '440', text: 'Когалым' },
        { value: '441', text: 'Кодинск' },
        { value: '442', text: 'Козельск' },
        { value: '443', text: 'Козловка' },
        { value: '444', text: 'Козьмодемьянск' },
        { value: '445', text: 'Кола' },
        { value: '446', text: 'Кологрив' },
        { value: '447', text: 'Коломна' },
        { value: '448', text: 'Колпашево' },
        { value: '449', text: 'Колпино' },
        { value: '450', text: 'Кольчугино' },
        { value: '451', text: 'Коммунар' },
        { value: '452', text: 'Комсомольск' },
        { value: '453', text: 'Комсомольск-на-Амуре' },
        { value: '454', text: 'Конаково' },
        { value: '455', text: 'Кондопога' },
        { value: '456', text: 'Кондрово' },
        { value: '457', text: 'Константиновск' },
        { value: '458', text: 'Копейск' },
        { value: '459', text: 'Кораблино' },
        { value: '460', text: 'Кореновск' },
        { value: '461', text: 'Коркино' },
        { value: '462', text: 'Королев' },
        { value: '463', text: 'Короча' },
        { value: '464', text: 'Корсаков' },
        { value: '465', text: 'Коряжма' },
        { value: '466', text: 'Костерево' },
        { value: '467', text: 'Костомукша' },
        { value: '468', text: 'Кострома' },
        { value: '469', text: 'Котельники' },
        { value: '470', text: 'Котельниково' },
        { value: '471', text: 'Котельнич' },
        { value: '472', text: 'Котлас' },
        { value: '473', text: 'Котово' },
        { value: '474', text: 'Котовск' },
        { value: '475', text: 'Кохма' },
        { value: '476', text: 'Красавино' },
        { value: '477', text: 'Красноармейск' },
        { value: '478', text: 'Красноармейск' },
        { value: '479', text: 'Красновишерск' },
        { value: '480', text: 'Красногорск' },
        { value: '481', text: 'Краснодар' },
        { value: '482', text: 'Красное Село' },
        { value: '483', text: 'Краснозаводск' },
        { value: '484', text: 'Краснознаменск' },
        { value: '485', text: 'Краснознаменск' },
        { value: '486', text: 'Краснокаменск' },
        { value: '487', text: 'Краснокамск' },
        { value: '488', text: 'Красноперекопск' },
        { value: '489', text: 'Красноперекопск' },
        { value: '490', text: 'Краснослободск' },
        { value: '491', text: 'Краснослободск' },
        { value: '492', text: 'Краснотурьинск' },
        { value: '493', text: 'Красноуральск' },
        { value: '494', text: 'Красноуфимск' },
        { value: '495', text: 'Красноярск' },
        { value: '496', text: 'Красный Кут' },
        { value: '497', text: 'Красный Сулин' },
        { value: '498', text: 'Красный Холм' },
        { value: '499', text: 'Кременки' },
        { value: '500', text: 'Кронштадт' },
        { value: '501', text: 'Кропоткин' },
        { value: '502', text: 'Крымск' },
        { value: '503', text: 'Кстово' },
        { value: '504', text: 'Кубинка' },
        { value: '505', text: 'Кувандык' },
        { value: '506', text: 'Кувшиново' },
        { value: '507', text: 'Кудымкар' },
        { value: '508', text: 'Кузнецк' },
        { value: '509', text: 'Кузнецк-12' },
        { value: '510', text: 'Кузнецк-8' },
        { value: '511', text: 'Куйбышев' },
        { value: '512', text: 'Кулебаки' },
        { value: '513', text: 'Кумертау' },
        { value: '514', text: 'Кунгур' },
        { value: '515', text: 'Купино' },
        { value: '516', text: 'Курган' },
        { value: '517', text: 'Курганинск' },
        { value: '518', text: 'Курильск' },
        { value: '519', text: 'Курлово' },
        { value: '520', text: 'Куровское' },
        { value: '521', text: 'Курск' },
        { value: '522', text: 'Куртамыш' },
        { value: '523', text: 'Курчатов' },
        { value: '524', text: 'Куса' },
        { value: '525', text: 'Кушва' },
        { value: '526', text: 'Кызыл' },
        { value: '527', text: 'Кыштым' },
        { value: '528', text: 'Кяхта' },
        { value: '529', text: 'Лабинск' },
        { value: '530', text: 'Лабытнанги' },
        { value: '531', text: 'Лагань' },
        { value: '532', text: 'Ладушкин' },
        { value: '533', text: 'Лаишево' },
        { value: '534', text: 'Лакинск' },
        { value: '535', text: 'Лангепас' },
        { value: '536', text: 'Лахденпохья' },
        { value: '537', text: 'Лебедянь' },
        { value: '538', text: 'Лениногорск' },
        { value: '539', text: 'Ленинск' },
        { value: '540', text: 'Ленинск-Кузнецкий' },
        { value: '541', text: 'Ленск' },
        { value: '542', text: 'Лермонтов' },
        { value: '543', text: 'Лесной' },
        { value: '544', text: 'Лесозаводск' },
        { value: '545', text: 'Лесосибирск' },
        { value: '546', text: 'Ливны' },
        { value: '547', text: 'Ликино-Дулево' },
        { value: '548', text: 'Липецк' },
        { value: '549', text: 'Липки' },
        { value: '550', text: 'Лиски' },
        { value: '551', text: 'Лихославль' },
        { value: '552', text: 'Лобня' },
        { value: '553', text: 'Лодейное Поле' },
        { value: '554', text: 'Ломоносов' },
        { value: '555', text: 'Лосино-Петровский' },
        { value: '556', text: 'Луга' },
        { value: '557', text: 'Луза' },
        { value: '558', text: 'Лукоянов' },
        { value: '559', text: 'Луховицы' },
        { value: '560', text: 'Лысково' },
        { value: '561', text: 'Лысьва' },
        { value: '562', text: 'Лыткарино' },
        { value: '563', text: 'Льгов' },
        { value: '564', text: 'Любань' },
        { value: '565', text: 'Люберцы' },
        { value: '566', text: 'Любим' },
        { value: '567', text: 'Людиново' },
        { value: '568', text: 'Лянтор' },
        { value: '569', text: 'Магадан' },
        { value: '570', text: 'Магас' },
        { value: '571', text: 'Магнитогорск' },
        { value: '572', text: 'Майкоп' },
        { value: '573', text: 'Майский' },
        { value: '574', text: 'Макаров' },
        { value: '575', text: 'Макарьев' },
        { value: '576', text: 'Макушино' },
        { value: '577', text: 'Малая Вишера' },
        { value: '578', text: 'Малгобек' },
        { value: '579', text: 'Малмыж' },
        { value: '580', text: 'Малоархангельск' },
        { value: '581', text: 'Малоярославец' },
        { value: '582', text: 'Мамадыш' },
        { value: '583', text: 'Мамоново' },
        { value: '584', text: 'Мантурово' },
        { value: '585', text: 'Мариинск' },
        { value: '586', text: 'Мариинский Посад' },
        { value: '587', text: 'Маркс' },
        { value: '588', text: 'Махачкала' },
        { value: '589', text: 'Мглин' },
        { value: '590', text: 'Мегион' },
        { value: '591', text: 'Медвежьегорск' },
        { value: '592', text: 'Медногорск' },
        { value: '593', text: 'Медынь' },
        { value: '594', text: 'Межгорье' },
        { value: '595', text: 'Междуреченск' },
        { value: '596', text: 'Мезень' },
        { value: '597', text: 'Меленки' },
        { value: '598', text: 'Мелеуз' },
        { value: '599', text: 'Менделеевск' },
        { value: '600', text: 'Мензелинск' },
        { value: '601', text: 'Мещовск' },
        { value: '602', text: 'Миасс' },
        { value: '603', text: 'Микунь' },
        { value: '604', text: 'Миллерово' },
        { value: '605', text: 'Минеральные Воды' },
        { value: '606', text: 'Минусинск' },
        { value: '607', text: 'Миньяр' },
        { value: '608', text: 'Мирный' },
        { value: '609', text: 'Мирный' },
        { value: '610', text: 'Михайлов' },
        { value: '611', text: 'Михайловка' },
        { value: '612', text: 'Михайловск' },
        { value: '613', text: 'Михайловск' },
        { value: '614', text: 'Мичуринск' },
        { value: '615', text: 'Могоча' },
        { value: '616', text: 'Можайск' },
        { value: '617', text: 'Можга' },
        { value: '618', text: 'Моздок' },
        { value: '619', text: 'Мончегорск' },
        { value: '620', text: 'Морозовск' },
        { value: '621', text: 'Моршанск' },
        { value: '622', text: 'Мосальск' },
        { value: '623', text: 'Москва' },
        { value: '624', text: 'Московский' },
        { value: '625', text: 'Московский' },
        { value: '626', text: 'Муравленко' },
        { value: '627', text: 'Мураши' },
        { value: '628', text: 'Мурманск' },
        { value: '629', text: 'Муром' },
        { value: '630', text: 'Мценск' },
        { value: '631', text: 'Мыски' },
        { value: '632', text: 'Мытищи' },
        { value: '633', text: 'Мышкин' },
        { value: '634', text: 'Набережные Челны' },
        { value: '635', text: 'Навашино' },
        { value: '636', text: 'Наволоки' },
        { value: '637', text: 'Надым' },
        { value: '638', text: 'Назарово' },
        { value: '639', text: 'Назрань' },
        { value: '640', text: 'Называевск' },
        { value: '641', text: 'Нальчик' },
        { value: '642', text: 'Нариманов' },
        { value: '643', text: 'Наро-Фоминск' },
        { value: '644', text: 'Нарткала' },
        { value: '645', text: 'Нарьян-Мар' },
        { value: '646', text: 'Находка' },
        { value: '647', text: 'Невель' },
        { value: '648', text: 'Невельск' },
        { value: '649', text: 'Невинномысск' },
        { value: '650', text: 'Невьянск' },
        { value: '651', text: 'Нелидово' },
        { value: '652', text: 'Неман' },
        { value: '653', text: 'Нерехта' },
        { value: '654', text: 'Нерчинск' },
        { value: '655', text: 'Нерюнгри' },
        { value: '656', text: 'Нестеров' },
        { value: '657', text: 'Нефтегорск' },
        { value: '658', text: 'Нефтекамск' },
        { value: '659', text: 'Нефтекумск' },
        { value: '660', text: 'Нефтеюганск' },
        { value: '661', text: 'Нея' },
        { value: '662', text: 'Нижневартовск' },
        { value: '663', text: 'Нижнекамск' },
        { value: '664', text: 'Нижнеудинск' },
        { value: '665', text: 'Нижние Серги' },
        { value: '666', text: 'Нижние Серги-3' },
        { value: '667', text: 'Нижний Ломов' },
        { value: '668', text: 'Нижний Новгород' },
        { value: '669', text: 'Нижний Тагил' },
        { value: '670', text: 'Нижняя Салда' },
        { value: '671', text: 'Нижняя Тура' },
        { value: '672', text: 'Николаевск' },
        { value: '673', text: 'Николаевск-на-Амуре' },
        { value: '674', text: 'Никольск' },
        { value: '675', text: 'Никольск' },
        { value: '676', text: 'Никольское' },
        { value: '677', text: 'Новая Ладога' },
        { value: '678', text: 'Новая Ляля' },
        { value: '679', text: 'Новоалександровск' },
        { value: '680', text: 'Новоалтайск' },
        { value: '681', text: 'Новоаннинский' },
        { value: '682', text: 'Нововоронеж' },
        { value: '683', text: 'Новодвинск' },
        { value: '684', text: 'Новозыбков' },
        { value: '685', text: 'Новокубанск' },
        { value: '686', text: 'Новокузнецк' },
        { value: '687', text: 'Новокуйбышевск' },
        { value: '688', text: 'Новомичуринск' },
        { value: '689', text: 'Новомосковск' },
        { value: '690', text: 'Новопавловск' },
        { value: '691', text: 'Новоржев' },
        { value: '692', text: 'Новороссийск' },
        { value: '693', text: 'Новосибирск' },
        { value: '694', text: 'Новосиль' },
        { value: '695', text: 'Новосокольники' },
        { value: '696', text: 'Новотроицк' },
        { value: '697', text: 'Новоузенск' },
        { value: '698', text: 'Новоульяновск' },
        { value: '699', text: 'Новоуральск' },
        { value: '700', text: 'Новохоперск' },
        { value: '701', text: 'Новочебоксарск' },
        { value: '702', text: 'Новочеркасск' },
        { value: '703', text: 'Новошахтинск' },
        { value: '704', text: 'Новый Оскол' },
        { value: '705', text: 'Новый Уренгой' },
        { value: '706', text: 'Ногинск' },
        { value: '707', text: 'Нолинск' },
        { value: '708', text: 'Норильск' },
        { value: '709', text: 'Ноябрьск' },
        { value: '710', text: 'Нурлат' },
        { value: '711', text: 'Нытва' },
        { value: '712', text: 'Нюрба' },
        { value: '713', text: 'Нягань' },
        { value: '714', text: 'Нязепетровск' },
        { value: '715', text: 'Няндома' },
        { value: '716', text: 'Облучье' },
        { value: '717', text: 'Обнинск' },
        { value: '718', text: 'Обоянь' },
        { value: '719', text: 'Обь' },
        { value: '720', text: 'Одинцово' },
        { value: '721', text: 'Ожерелье' },
        { value: '722', text: 'Озерск' },
        { value: '723', text: 'Озерск' },
        { value: '724', text: 'Озеры' },
        { value: '725', text: 'Октябрьск' },
        { value: '726', text: 'Октябрьский' },
        { value: '727', text: 'Окуловка' },
        { value: '728', text: 'Олекминск' },
        { value: '729', text: 'Оленегорск' },
        { value: '730', text: 'Оленегорск-1' },
        { value: '731', text: 'Оленегорск-2' },
        { value: '732', text: 'Оленегорск-4' },
        { value: '733', text: 'Олонец' },
        { value: '734', text: 'Омск' },
        { value: '735', text: 'Омутнинск' },
        { value: '736', text: 'Онега' },
        { value: '737', text: 'Опочка' },
        { value: '738', text: 'Орёл' },
        { value: '739', text: 'Оренбург' },
        { value: '740', text: 'Орехово-Зуево' },
        { value: '741', text: 'Орлов' },
        { value: '742', text: 'Орск' },
        { value: '743', text: 'Оса' },
        { value: '744', text: 'Осинники' },
        { value: '745', text: 'Осташков' },
        { value: '746', text: 'Остров' },
        { value: '747', text: 'Островной' },
        { value: '748', text: 'Острогожск' },
        { value: '749', text: 'Отрадное' },
        { value: '750', text: 'Отрадный' },
        { value: '751', text: 'Оха' },
        { value: '752', text: 'Оханск' },
        { value: '753', text: 'Очер' },
        { value: '754', text: 'Павлово' },
        { value: '755', text: 'Павловск' },
        { value: '756', text: 'Павловск' },
        { value: '757', text: 'Павловский Посад' },
        { value: '758', text: 'Палласовка' },
        { value: '759', text: 'Партизанск' },
        { value: '760', text: 'Певек' },
        { value: '761', text: 'Пенза' },
        { value: '762', text: 'Первомайск' },
        { value: '763', text: 'Первоуральск' },
        { value: '764', text: 'Перевоз' },
        { value: '765', text: 'Пересвет' },
        { value: '766', text: 'Переславль-Залесский' },
        { value: '767', text: 'Пермь' },
        { value: '768', text: 'Пестово' },
        { value: '769', text: 'Петергоф' },
        { value: '770', text: 'Петров Вал' },
        { value: '771', text: 'Петровск' },
        { value: '772', text: 'Петровск-Забайкальский' },
        { value: '773', text: 'Петрозаводск' },
        { value: '774', text: 'Петропавловск-Камчатский' },
        { value: '775', text: 'Петухово' },
        { value: '776', text: 'Петушки' },
        { value: '777', text: 'Печора' },
        { value: '778', text: 'Печоры' },
        { value: '779', text: 'Пикалево' },
        { value: '780', text: 'Пионерский' },
        { value: '781', text: 'Питкяранта' },
        { value: '782', text: 'Плавск' },
        { value: '783', text: 'Пласт' },
        { value: '784', text: 'Плес' },
        { value: '785', text: 'Поворино' },
        { value: '786', text: 'Подгорное' },
        { value: '787', text: 'Подольск' },
        { value: '788', text: 'Подпорожье' },
        { value: '789', text: 'Покачи' },
        { value: '790', text: 'Покров' },
        { value: '791', text: 'Покровск' },
        { value: '792', text: 'Полевской' },
        { value: '793', text: 'Полесск' },
        { value: '794', text: 'Полысаево' },
        { value: '795', text: 'Полярные Зори' },
        { value: '796', text: 'Полярный' },
        { value: '797', text: 'Поронайск' },
        { value: '798', text: 'Порхов' },
        { value: '799', text: 'Похвистнево' },
        { value: '800', text: 'Почеп' },
        { value: '801', text: 'Починок' },
        { value: '802', text: 'Пошехонье' },
        { value: '803', text: 'Правдинск' },
        { value: '804', text: 'Приволжск' },
        { value: '805', text: 'Приморск' },
        { value: '806', text: 'Приморск' },
        { value: '807', text: 'Приморско-Ахтарск' },
        { value: '808', text: 'Приозерск' },
        { value: '809', text: 'Прокопьевск' },
        { value: '810', text: 'Пролетарск' },
        { value: '811', text: 'Протвино' },
        { value: '812', text: 'Прохладный' },
        { value: '813', text: 'Псков' },
        { value: '814', text: 'Пугачев' },
        { value: '815', text: 'Пудож' },
        { value: '816', text: 'Пустошка' },
        { value: '817', text: 'Пучеж' },
        { value: '818', text: 'Пушкин' },
        { value: '819', text: 'Пушкино' },
        { value: '820', text: 'Пущино' },
        { value: '821', text: 'Пыталово' },
        { value: '822', text: 'Пыть-Ях' },
        { value: '823', text: 'Пятигорск' },
        { value: '824', text: 'Радужный' },
        { value: '825', text: 'Радужный' },
        { value: '826', text: 'Райчихинск' },
        { value: '827', text: 'Раменское' },
        { value: '828', text: 'Рассказово' },
        { value: '829', text: 'Ревда' },
        { value: '830', text: 'Реж' },
        { value: '831', text: 'Реутов' },
        { value: '832', text: 'Ржев' },
        { value: '833', text: 'Родники' },
        { value: '834', text: 'Рославль' },
        { value: '835', text: 'Россошь' },
        { value: '836', text: 'Ростов' },
        { value: '837', text: 'Ростов-на-Дону' },
        { value: '838', text: 'Рошаль' },
        { value: '839', text: 'Ртищево' },
        { value: '840', text: 'Рубцовск' },
        { value: '841', text: 'Рудня' },
        { value: '842', text: 'Руза' },
        { value: '843', text: 'Рузаевка' },
        { value: '844', text: 'Рыбинск' },
        { value: '845', text: 'Рыбное' },
        { value: '846', text: 'Рыльск' },
        { value: '847', text: 'Ряжск' },
        { value: '848', text: 'Рязань' },
        { value: '849', text: 'Саки' },
        { value: '850', text: 'Саки' },
        { value: '851', text: 'Салават' },
        { value: '852', text: 'Салаир' },
        { value: '853', text: 'Салехард' },
        { value: '854', text: 'Сальск' },
        { value: '855', text: 'Самара' },
        { value: '856', text: 'Санкт-Петербург' },
        { value: '857', text: 'Саранск' },
        { value: '858', text: 'Сарапул' },
        { value: '859', text: 'Саратов' },
        { value: '860', text: 'Саров' },
        { value: '861', text: 'Сасово' },
        { value: '862', text: 'Сатка' },
        { value: '863', text: 'Сафоново' },
        { value: '864', text: 'Саяногорск' },
        { value: '865', text: 'Саянск' },
        { value: '866', text: 'Светлогорск' },
        { value: '867', text: 'Светлоград' },
        { value: '868', text: 'Светлый' },
        { value: '869', text: 'Светогорск' },
        { value: '870', text: 'Свирск' },
        { value: '871', text: 'Свободный' },
        { value: '872', text: 'Себеж' },
        { value: '873', text: 'Севастополь' },
        { value: '874', text: 'Северобайкальск' },
        { value: '875', text: 'Северодвинск' },
        { value: '876', text: 'Северо-Курильск' },
        { value: '877', text: 'Североморск' },
        { value: '878', text: 'Североуральск' },
        { value: '879', text: 'Северск' },
        { value: '880', text: 'Севск' },
        { value: '881', text: 'Сегежа' },
        { value: '882', text: 'Сельцо' },
        { value: '883', text: 'Семенов' },
        { value: '884', text: 'Семикаракорск' },
        { value: '885', text: 'Семилуки' },
        { value: '886', text: 'Сенгилей' },
        { value: '887', text: 'Серафимович' },
        { value: '888', text: 'Сергач' },
        { value: '889', text: 'Сергиев Посад' },
        { value: '890', text: 'Сергиев Посад-7' },
        { value: '891', text: 'Сердобск' },
        { value: '892', text: 'Серов' },
        { value: '893', text: 'Серпухов' },
        { value: '894', text: 'Сертолово' },
        { value: '895', text: 'Сестрорецк' },
        { value: '896', text: 'Сибай' },
        { value: '897', text: 'Сим' },
        { value: '898', text: 'Симферополь' },
        { value: '899', text: 'Сковородино' },
        { value: '900', text: 'Скопин' },
        { value: '901', text: 'Славгород' },
        { value: '902', text: 'Славск' },
        { value: '903', text: 'Славянск-на-Кубани' },
        { value: '904', text: 'Сланцы' },
        { value: '905', text: 'Слободской' },
        { value: '906', text: 'Слюдянка' },
        { value: '907', text: 'Смоленск' },
        { value: '908', text: 'Снегири' },
        { value: '909', text: 'Снежинск' },
        { value: '910', text: 'Снежногорск' },
        { value: '911', text: 'Собинка' },
        { value: '912', text: 'Советск' },
        { value: '913', text: 'Советск' },
        { value: '914', text: 'Советск' },
        { value: '915', text: 'Советская Гавань' },
        { value: '916', text: 'Советский' },
        { value: '917', text: 'Сокол' },
        { value: '918', text: 'Солигалич' },
        { value: '919', text: 'Соликамск' },
        { value: '920', text: 'Солнечногорск' },
        { value: '921', text: 'Солнечногорск-2' },
        { value: '922', text: 'Солнечногорск-25' },
        { value: '923', text: 'Солнечногорск-30' },
        { value: '924', text: 'Солнечногорск-7' },
        { value: '925', text: 'Сольвычегодск' },
        { value: '926', text: 'Соль-Илецк' },
        { value: '927', text: 'Сольцы' },
        { value: '928', text: 'Сольцы 2' },
        { value: '929', text: 'Сорочинск' },
        { value: '930', text: 'Сорск' },
        { value: '931', text: 'Сортавала' },
        { value: '932', text: 'Сосенский' },
        { value: '933', text: 'Сосновка' },
        { value: '934', text: 'Сосновоборск' },
        { value: '935', text: 'Сосновый Бор' },
        { value: '936', text: 'Сосногорск' },
        { value: '937', text: 'Сочи' },
        { value: '938', text: 'Спас-Деменск' },
        { value: '939', text: 'Спас-Клепики' },
        { value: '940', text: 'Спасск' },
        { value: '941', text: 'Спасск-Дальний' },
        { value: '942', text: 'Спасск-Рязанский' },
        { value: '943', text: 'Среднеколымск' },
        { value: '944', text: 'Среднеуральск' },
        { value: '945', text: 'Сретенск' },
        { value: '946', text: 'Ставрополь' },
        { value: '947', text: 'Старая Купавна' },
        { value: '948', text: 'Старая Русса' },
        { value: '949', text: 'Старица' },
        { value: '950', text: 'Стародуб' },
        { value: '951', text: 'Старый крым' },
        { value: '952', text: 'Старый Оскол' },
        { value: '953', text: 'Стерлитамак' },
        { value: '954', text: 'Стрежевой' },
        { value: '955', text: 'Строитель' },
        { value: '956', text: 'Струнино' },
        { value: '957', text: 'Ступино' },
        { value: '958', text: 'Суворов' },
        { value: '959', text: 'Судак' },
        { value: '960', text: 'Суджа' },
        { value: '961', text: 'Судогда' },
        { value: '962', text: 'Суздаль' },
        { value: '963', text: 'Суоярви' },
        { value: '964', text: 'Сураж' },
        { value: '965', text: 'Сургут' },
        { value: '966', text: 'Суровикино' },
        { value: '967', text: 'Сурск' },
        { value: '968', text: 'Сусуман' },
        { value: '969', text: 'Сухиничи' },
        { value: '970', text: 'Сухой Лог' },
        { value: '971', text: 'Сызрань' },
        { value: '972', text: 'Сыктывкар' },
        { value: '973', text: 'Сысерть' },
        { value: '974', text: 'Сычевка' },
        { value: '975', text: 'Сясьстрой' },
        { value: '976', text: 'Тавда' },
        { value: '977', text: 'Таганрог' },
        { value: '978', text: 'Тайга' },
        { value: '979', text: 'Тайшет' },
        { value: '980', text: 'Талдом' },
        { value: '981', text: 'Талица' },
        { value: '982', text: 'Тамбов' },
        { value: '983', text: 'Тара' },
        { value: '984', text: 'Тарко-Сале' },
        { value: '985', text: 'Таруса' },
        { value: '986', text: 'Татарск' },
        { value: '987', text: 'Таштагол' },
        { value: '988', text: 'Тверь' },
        { value: '989', text: 'Теберда' },
        { value: '990', text: 'Тейково' },
        { value: '991', text: 'Темников' },
        { value: '992', text: 'Темрюк' },
        { value: '993', text: 'Терек' },
        { value: '994', text: 'Тетюши' },
        { value: '995', text: 'Тимашевск' },
        { value: '996', text: 'Тихвин' },
        { value: '997', text: 'Тихорецк' },
        { value: '998', text: 'Тобольск' },
        { value: '999', text: 'Тогучин' },
        { value: '1000', text: 'Тольятти' },
        { value: '1001', text: 'Томари' },
        { value: '1002', text: 'Томмот' },
        { value: '1003', text: 'Томск' },
        { value: '1004', text: 'Топки' },
        { value: '1005', text: 'Торжок' },
        { value: '1006', text: 'Торопец' },
        { value: '1007', text: 'Тосно' },
        { value: '1008', text: 'Тотьма' },
        { value: '1009', text: 'Трехгорный' },
        { value: '1010', text: 'Трехгорный-1' },
        { value: '1011', text: 'Троицк' },
        { value: '1012', text: 'Троицк' },
        { value: '1013', text: 'Трубчевск' },
        { value: '1014', text: 'Туапсе' },
        { value: '1015', text: 'Туймазы' },
        { value: '1016', text: 'Тула' },
        { value: '1017', text: 'Тулун' },
        { value: '1018', text: 'Туран' },
        { value: '1019', text: 'Туринск' },
        { value: '1020', text: 'Тутаев' },
        { value: '1021', text: 'Тында' },
        { value: '1022', text: 'Тырныауз' },
        { value: '1023', text: 'Тюкалинск' },
        { value: '1024', text: 'Тюмень' },
        { value: '1025', text: 'Уварово' },
        { value: '1026', text: 'Углегорск' },
        { value: '1027', text: 'Углич' },
        { value: '1028', text: 'Удачный' },
        { value: '1029', text: 'Удомля' },
        { value: '1030', text: 'Ужур' },
        { value: '1031', text: 'Узловая' },
        { value: '1032', text: 'Улан-Удэ' },
        { value: '1033', text: 'Ульяновск' },
        { value: '1034', text: 'Унеча' },
        { value: '1035', text: 'Урай' },
        { value: '1036', text: 'Урень' },
        { value: '1037', text: 'Уржум' },
        { value: '1038', text: 'Урус-Мартан' },
        { value: '1039', text: 'Урюпинск' },
        { value: '1040', text: 'Усинск' },
        { value: '1041', text: 'Усмань' },
        { value: '1042', text: 'Усолье' },
        { value: '1043', text: 'Усолье-Сибирское' },
        { value: '1044', text: 'Уссурийск' },
        { value: '1045', text: 'Усть-Джегута' },
        { value: '1046', text: 'Усть-Илимск' },
        { value: '1047', text: 'Усть-Катав' },
        { value: '1048', text: 'Усть-Кут' },
        { value: '1049', text: 'Усть-Лабинск' },
        { value: '1050', text: 'Устюжна' },
        { value: '1051', text: 'Уфа' },
        { value: '1052', text: 'Ухта' },
        { value: '1053', text: 'Учалы' },
        { value: '1054', text: 'Уяр' },
        { value: '1055', text: 'Фатеж' },
        { value: '1056', text: 'Феодосия' },
        { value: '1057', text: 'Фокино' },
        { value: '1058', text: 'Фокино' },
        { value: '1059', text: 'Фролово' },
        { value: '1060', text: 'Фрязино' },
        { value: '1061', text: 'Фурманов' },
        { value: '1062', text: 'Хабаровск' },
        { value: '1063', text: 'Хадыженск' },
        { value: '1064', text: 'Ханты-Мансийск' },
        { value: '1065', text: 'Харабали' },
        { value: '1066', text: 'Харовск' },
        { value: '1067', text: 'Хасавюрт' },
        { value: '1068', text: 'Хвалынск' },
        { value: '1069', text: 'Хилок' },
        { value: '1070', text: 'Химки' },
        { value: '1071', text: 'Холм' },
        { value: '1072', text: 'Холмск' },
        { value: '1073', text: 'Хотьково' },
        { value: '1074', text: 'Цивильск' },
        { value: '1075', text: 'Цимлянск' },
        { value: '1076', text: 'Чадан' },
        { value: '1077', text: 'Чайковский' },
        { value: '1078', text: 'Чапаевск' },
        { value: '1079', text: 'Чаплыгин' },
        { value: '1080', text: 'Чебаркуль' },
        { value: '1081', text: 'Чебоксары' },
        { value: '1082', text: 'Чегем' },
        { value: '1083', text: 'Чекалин' },
        { value: '1084', text: 'Челябинск' },
        { value: '1085', text: 'Чердынь' },
        { value: '1086', text: 'Черемхово' },
        { value: '1087', text: 'Черепаново' },
        { value: '1088', text: 'Череповец' },
        { value: '1089', text: 'Черкесск' },
        { value: '1090', text: 'Чермоз' },
        { value: '1091', text: 'Черноголовка' },
        { value: '1092', text: 'Черногорск' },
        { value: '1093', text: 'Чернушка' },
        { value: '1094', text: 'Черняховск' },
        { value: '1095', text: 'Чехов' },
        { value: '1096', text: 'Чехов-2' },
        { value: '1097', text: 'Чехов-3' },
        { value: '1098', text: 'Чехов-8' },
        { value: '1099', text: 'Чистополь' },
        { value: '1100', text: 'Чита' },
        { value: '1101', text: 'Чкаловск' },
        { value: '1102', text: 'Чудово' },
        { value: '1103', text: 'Чулым' },
        { value: '1104', text: 'Чулым-3' },
        { value: '1105', text: 'Чусовой' },
        { value: '1106', text: 'Чухлома' },
        { value: '1107', text: 'Шагонар' },
        { value: '1108', text: 'Шадринск' },
        { value: '1109', text: 'Шали' },
        { value: '1110', text: 'Шарыпово' },
        { value: '1111', text: 'Шарья' },
        { value: '1112', text: 'Шатура' },
        { value: '1113', text: 'Шахтерск' },
        { value: '1114', text: 'Шахты' },
        { value: '1115', text: 'Шахунья' },
        { value: '1116', text: 'Шацк' },
        { value: '1117', text: 'Шебекино' },
        { value: '1118', text: 'Шелехов' },
        { value: '1119', text: 'Шенкурск' },
        { value: '1120', text: 'Шилка' },
        { value: '1121', text: 'Шимановск' },
        { value: '1122', text: 'Шиханы' },
        { value: '1123', text: 'Шлиссельбург' },
        { value: '1124', text: 'Шумерля' },
        { value: '1125', text: 'Шумиха' },
        { value: '1126', text: 'Шуя' },
        { value: '1127', text: 'Щекино' },
        { value: '1128', text: 'Щелкино' },
        { value: '1129', text: 'Щелково' },
        { value: '1130', text: 'Щербинка' },
        { value: '1131', text: 'Щигры' },
        { value: '1132', text: 'Щучье' },
        { value: '1133', text: 'Электрогорск' },
        { value: '1134', text: 'Электросталь' },
        { value: '1135', text: 'Электроугли' },
        { value: '1136', text: 'Элиста' },
        { value: '1137', text: 'Энгельс' },
        { value: '1138', text: 'Энгельс-19' },
        { value: '1139', text: 'Энгельс-2' },
        { value: '1140', text: 'Эртиль' },
        { value: '1141', text: 'Юбилейный' },
        { value: '1142', text: 'Югорск' },
        { value: '1143', text: 'Южа' },
        { value: '1144', text: 'Южно-Сахалинск' },
        { value: '1145', text: 'Южно-Сухокумск' },
        { value: '1146', text: 'Южноуральск' },
        { value: '1147', text: 'Юрга' },
        { value: '1148', text: 'Юрьевец' },
        { value: '1149', text: 'Юрьев-Польский' },
        { value: '1150', text: 'Юрюзань' },
        { value: '1151', text: 'Юхнов' },
        { value: '1152', text: 'Юхнов-1' },
        { value: '1153', text: 'Юхнов-2' },
        { value: '1154', text: 'Ядрин' },
        { value: '1155', text: 'Якутск' },
        { value: '1156', text: 'Ялта' },
        { value: '1157', text: 'Ялуторовск' },
        { value: '1158', text: 'Янаул' },
        { value: '1159', text: 'Яранск' },
        { value: '1160', text: 'Яровое' },
        { value: '1161', text: 'Ярославль' },
        { value: '1162', text: 'Ярцево' },
        { value: '1163', text: 'Ясногорск' },
        { value: '1164', text: 'Ясный' },
        { value: '1165', text: 'Яхрома' },
      ],
      info: {
        name_family_status: 'unknown',
        cnt_children: '',
        cnt_fam_members: '',
        flag_own_car: false,
        own_car_age: '',
        flag_own_realty: false,
        name_housing_type: null,
        test: null,
        credit_date: '2019-12-26',
        organization_type: null,
        obl_options: null,
        cred_type: null,
        city_options: null,
        obl_fact: null,
        city_fact: null,
        obl_reg_check: false,
        city_reg_check: false,
        obl_reg: null,
        city_reg: null,
        obl_work_fact_check: false,
        obl_work_reg_check: false,
        city_work_fact_check: false,
        city_work_reg_check: false,
        obl_work: null,
        city_work: null,
        mobile: '',
        mobile_check: false,
        work_phone: '',
        home_phone: '',
        email: '',
        work_status: null,
        work_exp: '',
        position_cat: null,
        edu_type: null,
        own_inn: false,
        own_ndfl: false,
        own_snils: false,
        own_forepass: false,
        own_prev_app: false,
        goods_sum: '',
        cred_sum: '',
        credit_purpose: null,
        main_income: '',
        second_income: '',
      },
    };
  },
  computed: {
    state() {
      return this.value.length === 2;
    },
  },
  methods: {
    saveData(payload) {
      const path = 'http://localhost:5000/info/save';
      axios.post(path, payload)
        .then(() => {
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        user_hash: this.hash,
        info: {
          name_family_status: this.info.name_family_status,
          cnt_children: this.info.cnt_children,
          cnt_fam_members: this.info.cnt_fam_members,
          flag_own_car: this.info.flag_own_car,
          own_car_age: this.info.own_car_age,
          flag_own_realty: this.info.flag_own_realty,
          name_housing_type: this.info.name_housing_type,
          test: this.info.test,
          credit_date: this.info.credit_date,
          organization_type: this.info.organization_type,
          obl_options: this.info.obl_options,
          cred_type: this.info.cred_type,
          city_options: this.info.city_options,
          obl_fact: this.info.obl_fact,
          city_fact: this.info.city_fact,
          obl_reg_check: this.info.obl_reg_check,
          city_reg_check: this.info.city_reg_check,
          obl_reg: this.info.obl_reg,
          city_reg: this.info.city_reg,
          obl_work_fact_check: this.info.obl_work_fact_check,
          obl_work_reg_check: this.info.obl_work_reg_check,
          city_work_fact_check: this.info.city_work_fact_check,
          city_work_reg_check: this.info.city_work_reg_check,
          obl_work: this.info.obl_work,
          city_work: this.info.city_work,
          mobile: this.info.mobile,
          mobile_check: this.info.mobile_check,
          work_phone: this.info.work_phone,
          home_phone: this.info.home_phone,
          email: this.info.email,
          work_status: this.info.work_status,
          work_exp: this.info.work_exp,
          position_cat: this.info.position_cat,
          edu_type: this.info.edu_type,
          own_inn: this.info.own_inn,
          own_ndfl: this.info.own_ndfl,
          own_snils: this.info.own_snils,
          own_forepass: this.info.own_forepass,
          own_prev_app: this.info.own_prev_app,
          goods_sum: this.info.goods_sum,
          cred_sum: this.info.cred_sum,
          credit_purpose: this.info.credit_purpose,
          main_income: this.info.main_income,
          second_income: this.info.second_income,
        },
      };
      this.saveData(payload);
      this.predict();
    },
    loadData() {
      const payload = {
        user_hash: this.hash,
      };
      const path = 'http://localhost:5000/login/auth';
      axios.post(path, payload)
        .then((res) => {
          this.info.name_family_status = res.data.data.info.name_family_status;
          this.info.cnt_children = res.data.data.info.cnt_children;
          this.info.cnt_fam_members = res.data.data.info.cnt_fam_members;
          this.info.flag_own_car = res.data.data.info.flag_own_car;
          this.info.own_car_age = res.data.data.info.own_car_age;
          this.info.flag_own_realty = res.data.data.info.flag_own_realty;
          this.info.name_housing_type = res.data.data.info.name_housing_type;
          this.info.test = res.data.data.info.test;
          this.info.credit_date = res.data.data.info.credit_date;
          this.info.organization_type = res.data.data.info.organization_type;
          this.info.obl_options = res.data.data.info.obl_options;
          this.info.cred_type = res.data.data.info.cred_type;
          this.info.city_options = res.data.data.info.city_options;
          this.info.obl_fact = res.data.data.info.obl_fact;
          this.info.city_fact = res.data.data.info.city_fact;
          this.info.obl_reg_check = res.data.data.info.obl_reg_check;
          this.info.city_reg_check = res.data.data.info.city_reg_check;
          this.info.obl_reg = res.data.data.info.obl_reg;
          this.info.city_reg = res.data.data.info.city_reg;
          this.info.obl_work_fact_check = res.data.data.info.obl_work_fact_check;
          this.info.obl_work_reg_check = res.data.data.info.obl_work_reg_check;
          this.info.city_work_fact_check = res.data.data.info.city_work_fact_check;
          this.info.city_work_reg_check = res.data.data.info.city_work_reg_check;
          this.info.obl_work = res.data.data.info.obl_work;
          this.info.city_work = res.data.data.info.city_work;
          this.info.mobile = res.data.data.info.mobile;
          this.info.mobile_check = res.data.data.info.mobile_check;
          this.info.work_phone = res.data.data.info.work_phone;
          this.info.home_phone = res.data.data.info.home_phone;
          this.info.email = res.data.data.info.email;
          this.info.work_status = res.data.data.info.work_status;
          this.info.work_exp = res.data.data.info.work_exp;
          this.info.position_cat = res.data.data.info.position_cat;
          this.info.edu_type = res.data.data.info.edu_type;
          this.info.own_inn = res.data.data.info.own_inn;
          this.info.own_ndfl = res.data.data.info.own_ndfl;
          this.info.own_snils = res.data.data.info.own_snils;
          this.info.own_forepass = res.data.data.info.own_forepass;
          this.info.own_prev_app = res.data.data.info.own_prev_app;
          this.info.goods_sum = res.data.data.info.goods_sum;
          this.info.cred_sum = res.data.data.info.cred_sum;
          this.info.credit_purpose = res.data.data.info.credit_purpose;
          this.info.main_income = res.data.data.info.main_income;
          this.info.second_income = res.data.data.info.second_income;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    predict() {
      const load_path = 'http://localhost:5000/info/load';
      const load_payload = {
        user_hash: this.hash,
      };
      axios.post(load_path, load_payload)
        .then((res) => {
         const path = 'http://localhost:5000/model/predict';
          axios.post(path, res)
            .then((result) => {
              if (result.data.score >= 0.5) {
                alert('Вероятность одобрения кредита: ' + result.data.score + '. Кредит одобрен.');
              } else {
                alert('Вероятность одобрения кредита: ' + result.data.score + '. Кредит не одобрен.');
              }
            })
            .catch((error) => {
              // eslint-disable-next-line
              console.log(error);
            });
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
  },
  created() {
    this.loadData();
  },
};
</script>
