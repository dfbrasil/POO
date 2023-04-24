<template>
  <div class="card-detail-user-container">
    <div class="card-detail-user">
      <TextSimple :text="props.user.username" :styles="{ type: 'caption', color: 'neutral-white' }" />
      <div class="card-icons">
        <IconMicButton :size="16" :active="(props.user.id == id && microphone_status) ||
          props.user.mediastream?.microphone
          " />
        <IconHandButton :size="16" v-if="props.user.data.raisehand" :active="props.user.data.raisehand" />
        <IconMonitorButton v-if="Array.isArray(permissions) && permissions.includes('op')"
          @click="toggleScreenPermission(props.user.id)" :active="user.permissions.includes('allow-screen')" />
        <IconOptionsButton @click="openModal" :selected="modalIsOpen" :size="24" />
        <div v-if="privateMessageModalIsOpen" class="modal-background"></div>

       

        <ModalMenu v-if="modalIsOpen && props.user.mediastream?.screenshare" class="modal-menu-container" 
          @mouseleave="closeModal" @click="closeModal">
          <p class="p-style" @click="openPrivateMessageModal">Mensagem Privada</p>
          <p class="p-style" v-if="props.user.mediastream?.screenshare"  @click="pinScreen(props.user.id)">
            {{ isPinned ? 'Desfixar Tela' : 'Fixar Tela' }}
          </p>
        </ModalMenu>
        <ModalMenu v-if="modalIsOpen" class="modal-menu-container" 
          @mouseleave="closeModal" @click="closeModal">
          <p class="p-style" @click="openPrivateMessageModal">Mensagem Privada</p>
        </ModalMenu>
      
        
        <ModalMenu class="modal-private-message-container" v-if="privateMessageModalIsOpen"
          @mouseleave="closeModalOnMouseLeave" @click="closeModalOnMouseLeave">
          <ButtonIcon variation="red" class="close-button" @click.stop="privateMessageModalIsOpen = false;">
            <CloseButtom :size=" 18 " />
          </ButtonIcon>
          <TextSimple text="Enviar Mensagem Privada" :styles=" { type: 'caption', color: 'neutral-black' } " />
          <TextSimple class="txt-style" :text=" 'Para: ' + props.user.username "
            :styles=" { type: 'caption', color: 'neutral-black' } " />
          <InputTextArea type="text" v-model=" privateMessage " placeholder="Digite sua mensagem" :showPaperClip=" false "
            :showSender=" true " :isPrivateMessage=" true "
            @submit=" closePrivateMessageModal(props.user.id, privateMessage, $event) " @click.stop />
        </ModalMenu>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import InputTextArea from './InputTextArea.vue'
import { sendPrivateMessageTo } from '@/server/connection/chat/chat'
import useUserActions from '@/composables/connection/userActions';
import TextSimple from '../atoms/TextSimple.vue';
import IconHandButton from '../atoms/IconHandButton.vue';
import ModalMenu from "./ModalMenu.vue";
import useMediaStreams from '@/composables/connection/mediastream';
import IconMicButton from '../atoms/IconMicButton.vue';
import IconOptionsButton from '../atoms/IconOptionsButton.vue';
import IconMonitorButton from '../atoms/IconMonitorButton.vue';
import CloseButtom from '../atoms/CloseButtom.vue';
import type IUser from '@/types/User';
import { computed, defineEmits, ref, type PropType } from 'vue';
import useMe from '@/composables/connection/me';
import {
  allowAudio,
  forbidAudio,
  allowScreen,
  forbidScreen,
} from '@/server/connection/actions/permissions';
import { useStore } from 'vuex';

const { microphone_status, permissions, id } = useMe();
const store = useStore();
const activeTab = computed(() => store.state.displayStates.activeTab);
const modalIsOpen = ref(false);
const privateMessageModalIsOpen = ref(false);
const privateMessage = ref('');
const isPinned = ref(false);
const emitPinScreen = defineEmits<{ (event: 'pin-screen', userId: string): void }>();
// let showMsg : boolean = ref(false);

const props = defineProps({
  user: {
    type: Object as PropType<IUser>,
    required: true,
  },
  status: {
    type: String,
    required: true,
  },
  showMsg: {
    type: Boolean,
    default: true,
  },
});