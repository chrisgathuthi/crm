<template>
    <v-timeline align="start" class="bg-white">
        <v-timeline-item dot-color="primary">
            <template v-slot:opposite>
                Opposite content
            </template>
            <div>
                <div class="text-h6">Content title</div>
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
                    dolore magna aliqua.
                </p>
            </div>
        </v-timeline-item>

        <v-timeline-item>
            <template v-slot:opposite>
                Opposite content
            </template>
            <div>
                <div class="text-h6">Content title</div>
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
                    dolore magna aliqua.
                </p>
            </div>
        </v-timeline-item>

        <v-timeline-item dot-color="pink">
            <template v-slot:opposite>
                Opposite content
            </template>
            <div>
                <div class="text-h6">Content title</div>
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
                    dolore magna aliqua.
                </p>
            </div>
        </v-timeline-item>
    </v-timeline>
</template>