import { createVuetify } from 'vuetify'
import { sv } from 'vuetify/locale'
import DateFnsAdapter from '@date-io/date-fns'
import enUS from 'date-fns/locale/en-US'
import svSE from 'date-fns/locale/sv'

export const vuetify = createVuetify({
  locale: {
    messages: { sv },
  },
  date: {
    adapter: DateFnsAdapter,
    locale: {
      en: enUS,
      sv: svSE,
    },
  },
})
