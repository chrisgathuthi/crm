<script setup>
import Navigation from '@/components/Navigation.vue';
import StaffNavigation from '@/components/Navigation/StaffNavigation.vue';
import { onMounted, ref } from 'vue';
import {Converter} from '@/functions/DateConverter'
import axios from 'axios';
import { useFieldWorkStore } from '../stores/fieldwork'

// show summary
const expand = ref(false)

const store = useFieldWorkStore()
onMounted(async () => {
    await store.getFieldWorkList()
})

</script>
<template>
    <v-row>
        <v-col cols="3">
            <Navigation />

        </v-col>
        <v-col cols="9">
            <StaffNavigation />

            <v-row class="mt-8">
                <v-col>
                    <div class="subtitle">
                        Your tickets
                    </div>
                </v-col>
            </v-row>

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
                                    {{ item.location }}

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
                                    
                                </v-card-text>
                                <v-card-action>
                                    <v-btn elevation-1 block variant="outlined" class="w-50 my-3" prepend-icon="mdi-paperclip-plus">Materials</v-btn>
                                    
                                    <v-btn @click="closeTicket(item.id)" class="my-3" type="button" block 
                                        variant="outlined" >complete</v-btn>
                                    
                                </v-card-action>
                            </div>
                        </v-expand-transition>
                    </v-card-item>
                </v-card>
            </v-container>
            <v-container v-else>
                <h3>Hoorah! no Fieldwork Tickets</h3>

            </v-container>
        </v-col>
    </v-row>
</template>