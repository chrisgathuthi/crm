<script setup>
import { ref, onMounted } from 'vue';
import FieldWorkForm from '@/components/Dialog/FieldWorkForm.vue';
import { useFieldWorkStore } from '@/stores/fieldwork.js'
import { Converter } from '@/functions/DateConverter'

const dialog = ref(false)


// api call
const store = useFieldWorkStore()

// load before create phase
store.getFieldWorkList()
// show summary
const expand = ref(false)
// open/close ticket
const model = ref('no')
// show search
const search = ref(false)
</script>

<template>
    <v-card color="grey-lighten-4" flat height="auto" rounded="0">
        <v-toolbar density="comfortable">

            <v-toolbar-title>Field Tickets</v-toolbar-title>

            <v-spacer></v-spacer>
            <v-expand-x-transition>
                <div v-show="search" class="w-full">
                    <v-text-field hide-details single-line></v-text-field>
                </div>
            </v-expand-x-transition>

            <v-btn icon="mdi-magnify" @click="search = !search">
            </v-btn>
            <v-divider vertical></v-divider>

            <v-btn class="ml-2">
                completed tickets
            </v-btn>
            <v-divider vertical></v-divider>
            <v-btn color="primary" @click="dialog = !dialog" prepend-icon="mdi-plus">
                Tickets
                <FieldWorkForm :dialog="dialog" />
            </v-btn>
            <v-divider vertical></v-divider>

            <v-btn class="text-none" stacked>
                <v-badge content="2" color="error">
                    <v-icon>mdi-bell-outline</v-icon>
                </v-badge>
            </v-btn>
        </v-toolbar>
    </v-card>

    <!-- fieldwork data grid -->
    <v-infinite-scroll ref="infinite" height="500" side="end" @load="load">
        <v-container v-for="(item, index) in store.fieldworks" :key="index" v-if="store.fieldworks.length > 0">
            <v-card max-width="350" elevation="4">
                <v-card-item>
                    <v-card-title>
                        {{ item.task_name }}
                    </v-card-title>
                    <v-card-subtitle>
                        <v-row>
                            <v-col cols="auto">
                                {{ item.assignee }}
                            </v-col>
                            <v-divider vertical></v-divider>
                            <v-col cols="auto">
                                {{ Converter(item.date) }}
                            </v-col>
                            <v-col cols="auto">
                                status
                                <v-icon icon="mdi-circle-small" size="x-large" color="green-darken-2"></v-icon>
                            </v-col>
                        </v-row>
                    </v-card-subtitle>

                    <v-card-actions>
                        <v-btn @click="expand = !expand" class="bg-purple-accent-3"
                            :append-icon="expand ? 'mdi-chevron-up' : 'mdi-chevron-down'">
                            {{ !expand ? 'Read more' : 'Read less' }}
                        </v-btn>
                    </v-card-actions>

                    <v-expand-transition>
                        <div class="summary" v-show="expand">
                            <v-card-text>
                                {{ item.activities }}
                                <v-row>
                                    <v-col cols="auto">

                                        <v-switch v-model="model" hide-details true-value="closed" false-value="open"
                                            color="green" :label="`${model}`"></v-switch>
                                    </v-col>
                                </v-row>
                            </v-card-text>

                        </div>
                    </v-expand-transition>
                </v-card-item>
            </v-card>
        </v-container>
        <v-container v-else>
            <h3>Hoorah! no Fieldwork Tickets</h3>

        </v-container>
    </v-infinite-scroll>
</template>