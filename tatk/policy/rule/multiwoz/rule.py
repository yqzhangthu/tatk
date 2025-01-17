# -*- coding: utf-8 -*-
import torch
from tatk.policy.policy import Policy
from tatk.policy.rule.multiwoz.rule_based_multiwoz_bot import RuleBasedMultiwozBot
from tatk.policy.rule.multiwoz.policy_agenda_multiwoz import UserPolicyAgendaMultiWoz

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class Rule(Policy):
    
    def __init__(self, is_train=False, character='sys'):
        self.is_train = is_train
        self.character = character
        
        if character == 'sys':
            self.policy = RuleBasedMultiwozBot()
        elif character == 'usr':
            self.policy = UserPolicyAgendaMultiWoz()
        else:
            raise NotImplementedError('unknown character {}'.format(character))

    def predict(self, state):
        """
        Predict an system action given state.
        Args:
            state (dict): Dialog state. Please refer to util/state.py
        Returns:
            action : System act, with the form of (act_type, {slot_name_1: value_1, slot_name_2, value_2, ...})
        """
        return self.policy.predict(state)

    def init_session(self):
        """
        Restore after one session
        """
        self.policy.init_session()

    def is_terminal(self):
        if self.character == 'sys':
            return None
        return self.policy.is_terminal()

    def get_reward(self):
        if self.character == 'sys':
            return None
        return self.policy.get_reward()
